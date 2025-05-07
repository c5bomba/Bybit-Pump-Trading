# Bybit Telegram Signal Trading Bot

## Overview

This Python-based trading bot is designed to automate trades on the Bybit cryptocurrency exchange based on signals received from Telegram messages. It leverages the Telethon library to monitor a specified Telegram channel for buy (long) or sell (short) signals, and the PyBit library to interact with the Bybit API for order execution and account management.

The bot incorporates dynamic symbol handling, robust risk management, flexible exit strategies, and comprehensive pre-trade checks to ensure trades are placed according to user-defined parameters and exchange requirements. It supports both live and testnet environments.

## Key Features

*   **Telegram Integration:**
    *   Listens for new messages in a user-specified Telegram channel using Telethon.
    *   Filters messages based on configurable keywords (`keywords_long`, `keywords_short`) to identify trading signals.

*   **Dynamic Symbol & Instrument Management:**
    *   **Symbol Mapping:** Utilizes a `symbol_map` in `config.py` for user-defined shortcuts (e.g., `#btc` -> `BTCUSDT`, `pepe` -> `1000PEPEUSDT`).
    *   **Symbol Extraction:** Intelligently extracts trading symbols from messages by prioritizing the `symbol_map`, then checking for common prefixes (`#`, `$`), and finally attempting direct matches against known Bybit symbols (case-insensitive).
    *   **Live Instrument Data:** Periodically fetches (every 2 minutes) the official list of tradable instruments and their details (e.g., `tickSize`, `lotSizeFilter`, trading status) directly from the Bybit API (`/v5/market/instruments-info`). This ensures the bot always uses up-to-date information, removing reliance on static symbol files.

*   **Risk Management & Order Sizing:**
    *   Calculates order quantity based on a user-defined `equity_risk_percent` (percentage of total USDT equity to risk per trade) and a `price_stop_loss_percent` (percentage price movement against the position to trigger the stop-loss).
    *   The quantity calculation aims to risk a specific USDT amount if the stop-loss is hit.

*   **Order Execution & Management:**
    *   Places **Market Orders** on Bybit (Linear USDT Perpetuals).
    *   **Mandatory Stop-Loss:** Automatically places a stop-loss order along with the initial market order. The stop-loss price is calculated based on the entry price and `price_stop_loss_percent`, then formatted according to the instrument's `tickSize`.
    *   **Optional Take-Profit:** If `enable_take_profit` is true, calculates and places a take-profit order based on `price_take_profit_percent`. The take-profit price is also formatted to the instrument's `tickSize`.
    *   **Leverage:** Uses a `default_leverage` setting from `config.py` for all trades.
    *   **Testnet Support:** Easily switch between live trading and Bybit's testnet environment using the `use_testnet` flag and dedicated API keys in `config.py`.

*   **Flexible Exit Strategy:**
    *   If `enable_timed_exit` is `True` in `config.py`, the bot will attempt to close the position with a market order after `trade_cooldown_seconds`, regardless of SL/TP status.
    *   If `enable_timed_exit` is `False`, the position closure relies solely on the stop-loss or take-profit orders being triggered on the exchange.

*   **Pre-Trade Validations:**
    *   Checks if the extracted symbol is actively trading on Bybit based on the latest fetched instrument data.
    *   Adjusts the calculated quantity to comply with the symbol's `lotSizeFilter` (minimum trading quantity and quantity step).
    *   Verifies that the estimated USDT value of the order (quantity * price) meets Bybit's minimum order value requirement (currently hardcoded as 5 USDT but logged if skipped).

*   **Configuration:**
    *   All critical parameters, API keys, and preferences are managed externally in a `config.py` file for easy modification without altering the core script.

*   **Logging & Interaction:**
    *   Employs Python's `logging` module for detailed operational logs, providing insights into the bot's actions and decisions.
    *   Features a simple interactive command-line menu to start the listener, check Bybit wallet balance, and exit the application.

## Technologies Used

*   **Python 3.x**
*   **Telethon:** For interacting with the Telegram API.
*   **PyBit:** For interacting with the Bybit API (Unified Trading Account).
*   **Standard Python Libraries:** `asyncio`, `logging`, `decimal`.

## Setup and Configuration

1.  **Clone the Repository:**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Install Dependencies:**
    It's recommended to use a virtual environment.
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install telethon pybit python-dotenv # (Consider creating a requirements.txt with all dependencies)
    ```
    *(A `requirements.txt` file with `telethon`, `pybit`, and `python-dotenv` would simplify this step).*

3.  **Configure `config.py`:**
    Create a `config.py` file in the root directory of the project. This file stores all your sensitive information and trading parameters. **Do NOT commit this file to public repositories.**

    ```python
    # config.py

    # Telegram API Credentials
    api_id = 1234567  # Your Telegram API ID
    api_hash = 'YOUR_TELEGRAM_API_HASH'
    session_name = 'my_trading_bot_session' # Or any unique name for the Telethon session file
    phone_number = '+12345678900' # Optional: Your phone number if script needs it for login
    chat_id = -1001234567890 # ID of the Telegram channel/chat to listen to (can be a group ID too)

    # Bybit API Credentials & Settings
    # IMPORTANT: Generate separate API keys for Live and Testnet.
    # Ensure API key permissions include: Contract Trading (Order, Position) and Wallet (Account Info).
    use_testnet = True  # True for testnet, False for live trading

    live_api_key = "YOUR_LIVE_BYBIT_API_KEY"
    live_api_secret = "YOUR_LIVE_BYBIT_API_SECRET"

    testnet_api_key = "YOUR_TESTNET_BYBIT_API_KEY"
    testnet_api_secret = "YOUR_TESTNET_BYBIT_API_SECRET"

    default_leverage = "10" # Default leverage for trades (e.g., "10" for 10x)

    # Risk Management Parameters
    equity_risk_percent = 0.01  # e.g., 0.01 for 1% of total equity to risk per trade
    price_stop_loss_percent = 0.02  # e.g., 0.02 for a 2% price move against your entry for SL

    # Take-Profit Parameters
    enable_take_profit = True # True to enable TP orders, False to disable
    price_take_profit_percent = 0.04 # e.g., 0.04 for a 4% price move in your favor for TP

    # Timed Exit Strategy
    enable_timed_exit = False # True to enable timed exit, False to rely on SL/TP
    trade_cooldown_seconds = 300  # e.g., 300 for 5 minutes, only if enable_timed_exit is True

    # Signal Keywords (lowercase)
    keywords_long = ["long", "buy", "bullish"] # Keywords indicating a long signal
    keywords_short = ["short", "sell", "bearish"] # Keywords indicating a short signal

    # Symbol Mapping (lowercase input -> Official Bybit Symbol)
    # Add your custom shortcuts here.
    # Example: {"#btc": "BTCUSDT", "pepe": "1000PEPEUSDT", "$sol": "SOLUSDT"}
    symbol_map = {
        "btc": "BTCUSDT",
        "#btc": "BTCUSDT",
        "bitcoin": "BTCUSDT",
        "eth": "ETHUSDT",
        "#eth": "ETHUSDT",
        "ethereum": "ETHUSDT",
        "sol": "SOLUSDT",
        "$sol": "SOLUSDT",
        "pepe": "1000PEPEUSDT", # Bybit uses 1000PEPEUSDT for PEPE
        # Add more mappings as needed
    }

    # Time in force for orders (e.g., "GTC", "IOC", "FOK")
    time_in_force = "GTC" # GoodTillCancel is typical for market orders with SL/TP
    ```

4.  **First Run (Telegram Login):**
    The first time you run the script, Telethon will likely prompt you to log in to your Telegram account by entering your phone number and a code sent to you via Telegram. A session file (`session_name`.session) will be created to keep you logged in.

## Usage

1.  Ensure your `config.py` is correctly set up.
2.  Run the main script:
    ```bash
    python listenerV4.py
    ```
3.  The bot will display a menu:
    *   **1. Start Listening for Signals:** Connects to Telegram, fetches initial Bybit instrument data, and starts listening for messages in the configured channel.
    *   **2. Check Bybit Wallet Balance:** Fetches and displays your current USDT equity from Bybit.
    *   **3. Exit:** Stops the bot and disconnects from Telegram.

## Operational Notes

*   **Symbol Precision:** The bot uses `Decimal` for all financial calculations and fetches `tickSize` and `qtyStep` from Bybit to format order prices and quantities correctly.
*   **Error Handling:** Includes basic error handling for API requests and trade logic. Check the logs for detailed information.
*   **Minimum Order Value:** Bybit imposes minimum order values (e.g., 5 USDT). The bot checks this before placing an order and logs a warning if the condition isn't met.
*   **API Rate Limits:** Be mindful of Bybit API rate limits, especially if running multiple bots or making frequent non-trading calls. The periodic symbol update is set to 2 minutes, which should be conservative.

## Considerations

*   **Latency:** Trading performance, especially for market orders, can be affected by network latency between the machine running the bot, Telegram's servers, and Bybit's exchange servers. The bot's effectiveness is enhanced when these latencies are minimized.
*   **Signal Quality:** The bot's profitability is entirely dependent on the quality and timeliness of the signals received from the Telegram channel.
*   **Market Volatility:** High market volatility can lead to slippage on market orders and increase the risk of stop-loss orders being triggered unexpectedly.

## Disclaimer

**This trading bot is provided for educational and illustrative purposes only. Trading cryptocurrencies involves significant risk of financial loss. You are solely responsible for your trading decisions and any losses incurred.**

*   **No Financial Advice:** The software does not constitute financial advice.
*   **Use at Your Own Risk:** The developers and contributors are not liable for any financial losses or damages arising from the use of this software.
*   **Test Thoroughly:** Always test the bot extensively on Bybit's **testnet** with non-critical funds before considering live trading.
*   **Understand the Code:** Ensure you understand the code and its mechanisms before deploying it.
*   **Secure Your API Keys:** Keep your API keys confidential and secure. Do not share them or commit them to public repositories.

---
*This README is based on the bot's state as of the last update. Features and configurations may evolve.*

