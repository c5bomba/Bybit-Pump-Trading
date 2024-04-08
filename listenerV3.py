import json
from telethon import TelegramClient, events
from pybit.unified_trading import HTTP
from decimal import Decimal, ROUND_DOWN
import asyncio
import requests
from configg import *

with open('symbols.json', 'r') as infile:
    symbols_data = json.load(infile)

session = HTTP(
    testnet=False,
    api_key= bybit_api_key, 
    api_secret= bybit_api_secret
)
symbol=""
client = TelegramClient('session_name', api_id, api_hash)


client.start()

def extract_symbol(message):
    symbol_map = {
    '#aidoge': '10000000AIDOGEUSDT',
    '#coq': '10000COQ',
    '#ladys': '10000LADYS',
    '#nft': '10000NFT',
    '#sats': '10000SATS',
    '#starl': '10000STARL',
    '#wen': '10000WEN',
    '#bonk': '1000BONK',
    '#btt': '1000BTT',
    '#floki': '1000FLOKI',
    '#iq50': '1000IQ50',
    '#lunc': '1000LUNC',
    '#pepe': '1000PEPE',
    '#rats': '1000RATS',
    '#turbo': '1000TURBO',
    '#xec': '1000XEC',
    '$aidoge': '10000000AIDOGEUSDT',
    '$coq': '10000COQ',
    '$ladys': '10000LADYS',
    '$nft': '10000NFT',
    '$sats': '10000SATS',
    '$starl': '10000STARL',
    '$wen': '10000WEN',
    '$bonk': '1000BONK',
    '$btt': '1000BTT',
    '$floki': '1000FLOKI',
    '$iq50': '1000IQ50',
    '$lunc': '1000LUNC',
    '$pepe': '1000PEPE',
    '$rats': '1000RATS',
    '$turbo': '1000TURBO',
    '$xec': '1000XEC'
    }
    for word in message.split():
        word_lower = word.lower()
        if word_lower in symbol_map:
            return symbol_map[word_lower].upper()
        if word.startswith('$') or word.startswith('#'):
            symbol = word[1:]  # remove $ or # 
            if symbol.isalnum():  
                return symbol.upper()  # Upper letters
    return None


def get_balance():
    try:
        balance = session.get_wallet_balance(accountType="UNIFIED", coin="USDT")
        total_equity = balance['result']['list'][0]['totalEquity']
        return total_equity
    except Exception as err:
        print(err)

def qty_calculate(default_margin, default_leverage, last_price):
    decimal_default_margin = Decimal(default_margin)
    decimal_default_leverage = Decimal(default_leverage)
    qty = decimal_default_margin * decimal_default_leverage / last_price
    
    return qty
global balance
balance =get_balance()
print(f"Your balance: {balance} USDT")
print("_______________________________")

# Channel's id
channel_id = chat_id
@client.on(events.NewMessage(chats=channel_id))
async def my_event_handler(event):
    global balance, default_margin
    # receive message and print
    message = event.message.message
    print(message)
    symbol = extract_symbol(message)
    if symbol:
        print(f"Extracted symbol: {symbol}")
        keywordslong = ["bull", "bullish", "pump","buy high sell higher", "long","buy"]
        keywordsshort = ["bear", "bearish", "dump", "sell","short"]
        if any(keyword in message.lower() for keyword in keywordslong):
            print("Bullish sentiment detected, placing long order...")

            tickers = session.get_tickers(
                category="linear",
                symbol=symbol+"USDT",
            )           
            last_price = Decimal(tickers['result']['list'][0]['lastPrice'])
            print(f"Last price for {symbol}: {last_price}")           
            symbol=symbol+"USDT"
            if symbol in symbol_list:
                index = symbol_list.index(symbol)
                print(f"{index}th {symbol}.")
            else:
                print("Symbol not found.")

            try:
                symbol_info = symbols_data['result'][index]
                print("Min Qty:", symbol_info['lot_size_filter']['min_trading_qty'])
            except:
                print("Error:")

            qty = qty_calculate(default_margin, default_leverage, last_price)
            min_trading_qty = Decimal(str(symbol_info['lot_size_filter']['min_trading_qty']))
            newqty= min_trading_qty * (qty // min_trading_qty)
            print("Calculated qty:",newqty)       
            buy_order = session.place_order(
                category="linear",
                symbol=symbol,
                side="Buy",
                orderType="Market",
                qty=newqty,
                timeInForce="GoodTillCancel",
                isLeverage=0,
                orderFilter="Order",
                leverage=default_leverage,
            )
            print("BUY/OPEN")
            print(buy_order)

            await asyncio.sleep(11)  # 11 sec wait

            sell_order = session.place_order(
                category="linear",
                symbol=symbol,
                side="Sell",
                orderType="Market",
                qty=newqty,
                timeInForce="GoodTillCancel",
                isLeverage=0,
                orderFilter="ReduceOnly",
                leverage=default_leverage,
            )
            print("SELL/CLOSE")
            print(sell_order)
            newbalance = get_balance()
            newbalance = float(newbalance)
            balance = float(balance)

            difference = newbalance - balance
            margin_addition = round(difference, 1)

            print(f"Your new balance: {newbalance} USDT")
            print("Change is"+str(difference))
            default_margin += margin_addition
            print("_______________________________")      
            
        elif any(keyword in message.lower() for keyword in keywordsshort):
            print("Bearish sentiment detected, placing short order...")

            tickers = session.get_tickers(
                category="linear",
                symbol=symbol+"USDT",
            )           
            last_price = Decimal(tickers['result']['list'][0]['lastPrice'])
            
            print(f"Last price for {symbol}: {last_price}")
            symbol=symbol+"USDT"         
            
            if symbol in symbol_list:
                index = symbol_list.index(symbol)
                print(f"{index}th {symbol}.")
            else:
                print("Symbol not found")
            try:
                symbol_info = symbols_data['result'][index]
                print("Min Qty:", symbol_info['lot_size_filter']['min_trading_qty'])
            except:
                print("Error:")
            qty = qty_calculate(default_margin, default_leverage, last_price)
            min_trading_qty = Decimal(str(symbol_info['lot_size_filter']['min_trading_qty']))
            newqty= min_trading_qty * (qty // min_trading_qty)
            print("Calculated qty:",newqty)       
            sell_order = session.place_order(
                category="linear",
                symbol=symbol,
                side="Sell",
                orderType="Market",
                qty=newqty,
                timeInForce="GoodTillCancel",
                isLeverage=0,
                orderFilter="Order",
                leverage=default_leverage,
            )
            print("SELL/OPEN")
            print(sell_order)

            await asyncio.sleep(11)  # 11 sec wait
            buy_order = session.place_order(
                category="linear",
                symbol=symbol,
                side="Buy",
                orderType="Market",
                qty=newqty,
                timeInForce="GoodTillCancel",
                isLeverage=0,
                orderFilter="ReduceOnly",
                leverage=default_leverage,
            )
            
            print("BUY/CLOSE")
            print(buy_order)
            balance = float(balance)
            newbalance = get_balance()
            newbalance = float(newbalance)
            difference = newbalance - balance
            print(f"Your new balance: {newbalance} USDT")
            print("Change is"+str(difference))
            print("_______________________________")
        else:
            print("Sentiment not detected.")
        
    else:
        print("Symbol not found in message.")   
# Run code till disconnect
client.run_until_disconnected()
