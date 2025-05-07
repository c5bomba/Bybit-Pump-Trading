from telethon import TelegramClient, events
from pybit.unified_trading import HTTP
from decimal import Decimal, ROUND_DOWN, getcontext
import asyncio
import logging 
from config import *


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


symbols_data = {"result": []}
valid_symbols_list = []   
symbol_update_task = None   

# --- Initialize Bybit Session --- 
logger.info(f"Initializing Bybit session... Testnet Mode: {use_testnet}")
session = HTTP(
    testnet=use_testnet, # Set based on value from configg.py
    api_key= testnet_api_key if use_testnet else live_api_key, 
    api_secret= testnet_api_secret if use_testnet else live_api_secret
)


client = TelegramClient(session_name, api_id, api_hash) 

def extract_symbol(message, known_symbols):
    # 1. Check symbol_map from configg.py first
    words = message.split()
    for word in words:
        word_lower = word.lower()
        if word_lower in symbol_map:
            # Ensure the mapped symbol is actually valid/tradable
            if symbol_map[word_lower] in known_symbols:
                 logger.debug(f"Symbol map match: {word_lower} -> {symbol_map[word_lower]}")
                 return symbol_map[word_lower]
            else:
                 logger.warning(f"Symbol map match found ({word_lower} -> {symbol_map[word_lower]}) but symbol is not active/invalid.")

    # 2. Check for generic prefixes (# or $)
    for word in words:
        if word.startswith('$') or word.startswith('#'):
            base_symbol = word[1:]
            if base_symbol.isalnum():
                potential_symbol = base_symbol.upper()
                # Try adding USDT if it's likely a base coin
                if not potential_symbol.endswith("USDT") and not potential_symbol.endswith("USD"):
                    potential_symbol_usdt = potential_symbol + "USDT"
                    if potential_symbol_usdt in known_symbols:
                        logger.debug(f"Generic extraction (#/$), appended USDT: {word} -> {potential_symbol_usdt}")
                        return potential_symbol_usdt
                # Check if the symbol as-is (e.g., #BTCUSD) is valid
                if potential_symbol in known_symbols:
                    logger.debug(f"Generic extraction (#/$), direct: {word} -> {potential_symbol}")
                    return potential_symbol

    # 3. Check if any word directly matches a known symbol (case-insensitive)
    for word in words:
        potential_symbol_direct = word.upper()
        if potential_symbol_direct in known_symbols:
            logger.debug(f"Direct symbol match found: {word} -> {potential_symbol_direct}")
            return potential_symbol_direct

    logger.debug("No known or valid symbol format found in the message.")
    return None


def get_wallet_balance_equity():
    try:
        response = session.get_wallet_balance(accountType="UNIFIED", coin="USDT")
        if response and response.get('retCode') == 0 and response.get('result') and response['result'].get('list'):
            account_list = response['result']['list']
            if account_list:
                 total_equity_str = account_list[0].get('totalEquity', "0")
                 logger.info(f"Wallet balance (Equity) retrieved: {total_equity_str} USDT")
                 return Decimal(total_equity_str)
            else:
                 logger.error(f"Failed to get balance: Result list is empty. Response: {response}")
                 return Decimal("0")
        logger.error(f"Failed to get balance: {response}")
        return Decimal("0")
    except Exception as err:
        logger.exception(f"Exception in get_wallet_balance_equity: {err}")
        return Decimal("0")

def calculate_qty_for_target_risk(total_equity: Decimal, entry_price: Decimal, 
                                    price_stop_loss_percent: Decimal, 
                                    equity_risk_percent: Decimal):
    if entry_price <= 0:
        logger.warning("Entry price is zero or negative, cannot calculate quantity.")
        return Decimal(0)
    if total_equity <= 0:
        logger.warning("Total equity is zero or negative, cannot calculate quantity.")
        return Decimal(0)

    amount_to_risk_abs = total_equity * equity_risk_percent 
    price_change_at_stop_abs = entry_price * price_stop_loss_percent 
    
    if price_change_at_stop_abs <= 0:
        logger.warning("Price change at stop is zero or negative, cannot calculate quantity.")
        return Decimal(0)
        
    calculated_qty = amount_to_risk_abs / price_change_at_stop_abs
    logger.info(f"Risk Calculation: Equity={total_equity:.4f}, Risk%={equity_risk_percent*100:.2f}%, SL%={price_stop_loss_percent*100:.2f}%, Entry={entry_price}")
    logger.info(f"Calculated Raw Quantity (Qty): {calculated_qty}")
    return calculated_qty

current_total_equity = Decimal("0") 

channel_id = chat_id # from configg.py

@client.on(events.NewMessage(chats=channel_id))
async def my_event_handler(event):
    global current_total_equity, symbols_data, valid_symbols_list 

    message_text = event.message.message
    logger.info(f"New message received: {message_text}")
    
    extracted_trade_symbol = extract_symbol(message_text, valid_symbols_list)

    if not extracted_trade_symbol:
        logger.info("No valid symbol found in the message.")
        return

    logger.info(f"Extracted symbol: {extracted_trade_symbol}")

    symbol_info_json = next((s_info for s_info in symbols_data.get('list', []) 
                             if s_info.get('symbol') == extracted_trade_symbol), None)

    if not symbol_info_json or symbol_info_json.get('status') != 'Trading':
        logger.warning(f"Details not found or symbol not trading for {extracted_trade_symbol} (current API data). Skipping.")
        return

    # Fetch current price
    try:
        tickers_response = session.get_tickers(category="linear", symbol=extracted_trade_symbol)
        if not (tickers_response and tickers_response.get('retCode') == 0 and 
                tickers_response.get('result') and tickers_response['result'].get('list') and 
                len(tickers_response['result']['list']) > 0):
            logger.error(f"Could not get ticker data or list is empty for {extracted_trade_symbol}. Response: {tickers_response}")
            return
            
        ticker_data = tickers_response['result']['list'][0]
        if 'lastPrice' not in ticker_data:
             logger.error(f"Ticker data received for {extracted_trade_symbol} but 'lastPrice' key is missing. Response: {tickers_response}")
             return
             
        last_price_str = ticker_data['lastPrice']
        last_price = Decimal(last_price_str)
        if last_price <= Decimal(0):
             logger.warning(f"Invalid last price ({last_price}) for {extracted_trade_symbol}. Skipping.")
             return
        logger.info(f"Last price for {extracted_trade_symbol}: {last_price}")
    except Exception as e:
        logger.exception(f"Error fetching/parsing ticker for {extracted_trade_symbol}: {e}")
        return
        
    current_stop_loss_price_percentage = Decimal(str(price_stop_loss_percent))
    current_equity_to_risk_percentage = Decimal(str(equity_risk_percent))

    # --- Calculate Quantity --- 
    raw_qty = calculate_qty_for_target_risk(
        current_total_equity, 
        last_price,
        current_stop_loss_price_percentage, 
        current_equity_to_risk_percentage 
    )

    if raw_qty <= 0:
        logger.warning(f"Calculated quantity is {raw_qty}. Skipping trade for {extracted_trade_symbol}.")
        return

    # --- Adjust Qty based on Lot Size Filter --- 
    lot_size_filter = symbol_info_json.get('lotSizeFilter') or symbol_info_json.get('lot_size_filter')

    if not lot_size_filter:
        logger.error(f"Lot size filter key ('lotSizeFilter' or 'lot_size_filter') not found for {extracted_trade_symbol}. API response: {symbol_info_json}. Skipping trade.")
        return
        
    min_qty_str = lot_size_filter.get('minTradingQty') or lot_size_filter.get('min_trading_qty') or lot_size_filter.get('minOrderQty')
    qty_step_str = lot_size_filter.get('qtyStep') or lot_size_filter.get('qty_step')

    if min_qty_str is None or qty_step_str is None:
        logger.error(f"Lot filter keys (minTradingQty/qtyStep etc.) missing for {extracted_trade_symbol}. Filter: {lot_size_filter}. Skipping trade.")
        return

    try:
        min_qty_from_filter = Decimal(str(min_qty_str))
        qty_step_from_filter = Decimal(str(qty_step_str))
    except Exception as dec_err:
        logger.error(f"Could not convert lot filter values to Decimal for {extracted_trade_symbol} (min: {min_qty_str}, step: {qty_step_str}). Error: {dec_err}. Skipping trade.")
        return

    if qty_step_from_filter > 0:
        final_qty_to_trade = (raw_qty // qty_step_from_filter) * qty_step_from_filter
    else:
        logger.warning(f"qty_step is 0 for {extracted_trade_symbol}! Using raw quantity {raw_qty}.")
        final_qty_to_trade = raw_qty 

    final_qty_to_trade = Decimal(str(final_qty_to_trade))

    if final_qty_to_trade < min_qty_from_filter:
        logger.warning(f"Adjusted quantity {final_qty_to_trade} < min_trading_qty {min_qty_from_filter} ({extracted_trade_symbol}). Skipping trade.")
        return
    
    if final_qty_to_trade <= Decimal(0):
        logger.warning(f"Final quantity to trade is zero or less after adjustments for {extracted_trade_symbol}. Skipping trade.")
        return

    # --- Check Minimum Order Value --- 
    estimated_order_value = final_qty_to_trade * last_price
    min_required_order_value = Decimal('5') # Hardcoded based on Bybit error, consider making configurable
    
    if estimated_order_value < min_required_order_value:
        logger.warning(f"Estimated order value ({estimated_order_value:.4f} USDT) is below minimum required ({min_required_order_value} USDT). Skipping trade for {extracted_trade_symbol}.")
        return

    logger.info(f"Min Qty (Lot Filter): {min_qty_from_filter}, Qty Step: {qty_step_from_filter}")
    logger.info(f"Final Quantity to trade (after filters): {final_qty_to_trade}")

    # --- Determine Trade Side --- 
    trade_side = None
    if any(keyword in message_text.lower() for keyword in keywords_long):
        trade_side = "Buy"
        logger.info("Bullish signal detected, preparing LONG order...")
    elif any(keyword in message_text.lower() for keyword in keywords_short):
        trade_side = "Sell"
        logger.info("Bearish signal detected, preparing SHORT order...")
    else:
        logger.info("No Buy/Sell signal keywords found in the message.")
        return

    # --- Calculate and Format Stop-Loss --- 
    stop_loss_price_str = None
    try:
        price_filter = symbol_info_json.get('priceFilter') or symbol_info_json.get('price_filter')
        if not price_filter: raise ValueError("priceFilter not found")
        tick_size_str = price_filter.get('tickSize') or price_filter.get('tick_size')
        if not tick_size_str: raise ValueError("tickSize not found")

        if trade_side == "Buy":
            sl_price = last_price * (Decimal(1) - current_stop_loss_price_percentage)
            if sl_price >= last_price:
                 logger.error(f"Calculated Long SL price ({sl_price}) is not below entry price ({last_price}). Skipping trade.")
                 return
        elif trade_side == "Sell":
            sl_price = last_price * (Decimal(1) + current_stop_loss_price_percentage)
            if sl_price <= last_price:
                 logger.error(f"Calculated Short SL price ({sl_price}) is not above entry price ({last_price}). Skipping trade.")
                 return
        else:
             logger.error("Invalid trade side for Stop Loss calculation.")
             return

        stop_loss_price_str = format_price(sl_price, tick_size_str)
        logger.info(f"Calculated Stop Loss Price: {sl_price:.{abs(Decimal(tick_size_str).as_tuple().exponent)}f} -> Formatted: {stop_loss_price_str}") # Log raw SL with appropriate precision

    except Exception as sl_calc_err:
        logger.error(f"Error calculating/formatting Stop Loss for {extracted_trade_symbol}: {sl_calc_err}. API Response: {symbol_info_json}. Skipping trade.")
        return
        
    # --- Calculate and Format Take-Profit (if enabled) --- 
    take_profit_price_str = None
    temp_enable_take_profit = enable_take_profit
    if temp_enable_take_profit:
        try:
            price_filter = symbol_info_json.get('priceFilter') or symbol_info_json.get('price_filter')
            if not price_filter: raise ValueError("priceFilter not found")
            tick_size_str = price_filter.get('tickSize') or price_filter.get('tick_size')
            if not tick_size_str: raise ValueError("tickSize not found")
            
            current_take_profit_percent = Decimal(str(price_take_profit_percent))
            if current_take_profit_percent <= 0:
                 raise ValueError("price_take_profit_percent must be positive")

            if trade_side == "Buy":
                tp_price = last_price * (Decimal(1) + current_take_profit_percent)
                if tp_price <= last_price:
                     logger.warning(f"Calculated Long TP price ({tp_price}) is not above entry price ({last_price}). Disabling TP for this trade.")
                     temp_enable_take_profit = False
            elif trade_side == "Sell":
                tp_price = last_price * (Decimal(1) - current_take_profit_percent)
                if tp_price >= last_price:
                     logger.warning(f"Calculated Short TP price ({tp_price}) is not below entry price ({last_price}). Disabling TP for this trade.")
                     temp_enable_take_profit = False
            else:
                logger.error("Invalid trade side for Take Profit calculation.")
                temp_enable_take_profit = False
            
            if temp_enable_take_profit:
                 take_profit_price_str = format_price(tp_price, tick_size_str)
                 logger.info(f"Calculated Take Profit Price: {tp_price:.{abs(Decimal(tick_size_str).as_tuple().exponent)}f} -> Formatted: {take_profit_price_str}") # Log raw TP with appropriate precision

        except Exception as tp_calc_err:
            logger.error(f"Error calculating/formatting Take Profit for {extracted_trade_symbol}: {tp_calc_err}. Disabling TP for this trade.")
            temp_enable_take_profit = False 
            take_profit_price_str = None 

    # --- Execute Trade Cycle --- 
    balance_before_trade = current_total_equity
    log_sl_tp_info = f"SL: {stop_loss_price_str}" + (f", TP: {take_profit_price_str}" if temp_enable_take_profit and take_profit_price_str else ", TP: None")
    logger.info(f"Starting trade cycle: {trade_side} {final_qty_to_trade} {extracted_trade_symbol}. {log_sl_tp_info}. Balance Before: {balance_before_trade:.4f} USDT")

    try:
        open_order_side = trade_side
        close_order_side = "Sell" if trade_side == "Buy" else "Buy"
        
        order_params = {
            "category": "linear",
            "symbol": extracted_trade_symbol,
            "side": open_order_side,
            "orderType": "Market",
            "qty": str(final_qty_to_trade),
            "timeInForce": time_in_force,
            "isLeverage": 0,
            "orderFilter": "Order",
            "leverage": str(default_leverage),
            "stopLoss": stop_loss_price_str 
        }
        if temp_enable_take_profit and take_profit_price_str:
             order_params["takeProfit"] = take_profit_price_str

        logger.info(f"Placing {open_order_side} (OPEN) order for {final_qty_to_trade} {extracted_trade_symbol} @ Market. Params: {order_params}")
        open_order_response = session.place_order(**order_params)
        
        logger.info(f"{open_order_side.upper()}/OPEN Response (SL/TP): {open_order_response}")
        if not (open_order_response and open_order_response.get('retCode') == 0):
            error_msg = open_order_response.get('retMsg', 'No error message') if open_order_response else 'No response'
            logger.error(f"Failed to open {open_order_side} order: {error_msg}. Full Response: {open_order_response}") # Log full response on error
            return 
        else:
            logger.info(f"{open_order_side} order placed successfully.")

        # --- Timed Exit Logic (If Enabled) --- 
        if enable_timed_exit:
            logger.info(f"Timed exit enabled. Waiting {trade_cooldown_seconds} seconds before placing closing order...")
            await asyncio.sleep(trade_cooldown_seconds)

            logger.info(f"Placing {close_order_side} (CLOSE - Timed) order for {final_qty_to_trade} {extracted_trade_symbol} @ Market Price")
            # Check if position still exists before attempting to close (SL/TP might have triggered)
            # Note: This requires fetching position info, adding complexity. 
            # For now, we attempt the close anyway; it might fail if already closed.
            close_order_response = session.place_order(
                category="linear",
                symbol=extracted_trade_symbol,
                side=close_order_side,
                orderType="Market",
                qty=str(final_qty_to_trade), 
                timeInForce=time_in_force, 
                isLeverage=0,
                orderFilter="ReduceOnly",
                leverage=str(default_leverage) 
            )
            logger.info(f"{close_order_side.upper()}/CLOSE (Timed) Response: {close_order_response}")
            if not (close_order_response and close_order_response.get('retCode') == 0):
                error_msg = close_order_response.get('retMsg', 'No error message') if close_order_response else 'No response'
                # Log as warning if it's likely already closed by SL/TP (e.g., order not found error)
                # Specific error codes might need checking here.
                if "Order does not exist" in error_msg or "order not found" in error_msg: # Example check
                     logger.warning(f"Timed closing order ({close_order_side}) failed, likely already closed by SL/TP: {error_msg}")
                else:
                     logger.error(f"Failed to place timed closing order ({close_order_side}): {error_msg}. Full Response: {close_order_response}")
            else:
                logger.info(f"Timed closing order ({close_order_side}) placed successfully.")
        else:
             logger.info("Timed exit disabled. Position will close via SL or TP.")

    except Exception as e:
        logger.exception(f"An error occurred during trade execution for {extracted_trade_symbol}: {e}")
    finally:
        # Update balance and report P&L
        logger.info("Updating balance after trade cycle attempt...")
        new_total_equity = get_wallet_balance_equity()
        pnl_for_this_trade = new_total_equity - balance_before_trade
        
        current_total_equity = new_total_equity 

        logger.info(f"Balance before this trade: {balance_before_trade:.4f} USDT")
        logger.info(f"New total equity after trade: {current_total_equity:.4f} USDT")
        logger.info(f"P&L for this trade cycle: {pnl_for_this_trade:.4f} USDT")
        logger.info("_______________________________")

async def fetch_instrument_info():
    """Fetches and updates instrument info from Bybit API."""
    global symbols_data, valid_symbols_list
    try:
        logger.debug("Fetching instrument info from Bybit API...")
        response = session.get_instruments_info(category="linear")
        if response and response.get('retCode') == 0 and response.get('result') and response['result'].get('list'):
            new_symbols_data = response['result']
            new_valid_symbols = [s.get('symbol') for s in new_symbols_data.get('list', []) 
                               if s.get('status') == 'Trading' and s.get('symbol')]
            
            if not new_valid_symbols:
                 logger.warning("Instrument info fetched, but no active symbols found or list empty.")
                 return False
            
            symbols_data = new_symbols_data
            valid_symbols_list = new_valid_symbols
            logger.debug(f"Instrument info updated. {len(valid_symbols_list)} active symbols found.")
            return True
        else:
            logger.error(f"Failed to fetch instrument info or invalid response. Response: {response}")
            return False
    except Exception as e:
        logger.exception(f"Error fetching instrument info: {e}")
        return False

def format_price(price: Decimal, tick_size_str: str) -> str:
    """Formats the price according to the instrument's tick size."""
    try:
        tick_size = Decimal(tick_size_str)
        if tick_size <= 0:
            logger.warning(f"Invalid tick size ({tick_size_str}), cannot format price: {price}")
            # Fallback: return price with high precision
            return str(price.quantize(Decimal('1E-8')))
        
        decimal_places = abs(tick_size.as_tuple().exponent)
        # Round down for safety (esp. for SL)
        formatted_price = price.quantize(Decimal('1e-' + str(decimal_places)), rounding=ROUND_DOWN)
        return "{:.{dp}f}".format(formatted_price, dp=decimal_places)
    except Exception as format_err:
         logger.error(f"Error formatting price {price} with tick size {tick_size_str}: {format_err}")
         # Fallback: return price with high precision
         return str(price.quantize(Decimal('1E-8')))

async def update_symbols_periodically(interval_seconds=120):
    """Periodically fetches instrument info in the background."""
    while True:
        await fetch_instrument_info()
        try:
            await asyncio.sleep(interval_seconds)
        except asyncio.CancelledError:
            logger.info("Symbol update task cancelled.")
            break 
        except Exception as e:
             logger.exception(f"Error during sleep in update_symbols_periodically: {e}")
             await asyncio.sleep(interval_seconds)

async def start_listening_session():
    """Handles the listening process and periodic updates."""
    global current_total_equity, symbol_update_task
    
    # --- Connect to Telegram --- 
    if not client.is_connected():
        logger.info("Connecting to Telegram...")
        try:
            await client.start(phone=phone_number if phone_number else None) 
            logger.info("Telegram connection successful.")
        except Exception as e:
            logger.exception(f"Failed to start Telegram client: {e}")
            return
            
    if not await client.is_user_authorized():
        logger.error("Telegram user is not authorized. Please complete the login process.")
        return

    # --- Initial Data Fetch --- 
    logger.info("Fetching initial instrument info...")
    initial_fetch_success = await fetch_instrument_info()
    if not initial_fetch_success:
        logger.error("Failed to fetch initial instrument info. Bot cannot start.")
        if client.is_connected(): await client.disconnect() 
        return
        
    current_total_equity = get_wallet_balance_equity() 
    logger.info(f"Listener starting. Initial equity: {current_total_equity:.4f} USDT")
    
    # --- Start Periodic Update Task --- 
    logger.info(f"Starting periodic symbol update task (interval: {120} seconds).")
    symbol_update_task = asyncio.create_task(update_symbols_periodically(120))

    logger.info("Waiting for messages... Press Ctrl+C to stop.")
    logger.info("_______________________________")
    
    try:
        await client.run_until_disconnected()
    except KeyboardInterrupt:
        logger.info("\nListener stopped by user (Ctrl+C).")
    except Exception as e:
        logger.exception(f"Listener stopped due to an error: {e}")
    finally:
        logger.info("Listener session ending...")
        # --- Cancel Periodic Task --- 
        if symbol_update_task and not symbol_update_task.done():
            logger.info("Cancelling periodic symbol update task...")
            symbol_update_task.cancel()
            try:
                await symbol_update_task 
            except asyncio.CancelledError:
                 logger.info("Symbol update task successfully cancelled.")
            except Exception as task_cancel_e:
                 logger.exception(f"Error while cancelling symbol update task: {task_cancel_e}")
                 
        if client.is_connected():
            await client.disconnect()
            logger.info("Disconnected from Telegram.")


async def main_menu_async():
    """Runs the main interactive menu."""
    while True:
        print("\nMain Menu:") 
        print("1. Start Listening for Signals")
        print("2. Check Bybit Wallet Balance")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ").strip()

        if choice == '1':
            await start_listening_session()
        
        elif choice == '2':
            logger.info("Checking Bybit wallet balance...")
            balance = get_wallet_balance_equity()
            print(f"Current Bybit USDT Wallet Equity: {balance:.4f} USDT")
        
        elif choice == '3':
            logger.info("Exiting application...")
            if client.is_connected():
                await client.disconnect()
                # logger.info("Disconnected from Telegram.") # Already logged in finally block
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 3.") 

if __name__ == '__main__':
    logger.info("Starting Bybit Signal Trading Bot...")
    
    try:
        asyncio.run(main_menu_async())
    except Exception as main_err:
        logger.exception(f"An unexpected error occurred in the main application: {main_err}")
    finally:
        logger.info("Application has exited.")
