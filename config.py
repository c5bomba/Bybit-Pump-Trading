phone_number = ""
api_id = 11111111 #change this
api_hash = ""
chat_id =  -1111111111 #telegram group chat id

# --- Account Settings --- 
use_testnet = False # Set to True to use Testnet, False for Live account

# Live Account API Keys (used if use_testnet=False)
live_api_key = "" # REPLACE WITH YOUR LIVE API KEY
live_api_secret = "" # REPLACE WITH YOUR LIVE API SECRET
session_name = "session_name" # Telegram session file name

# Testnet Account API Keys (used if use_testnet=True)
testnet_api_key = "" # REPLACE WITH YOUR TESTNET API KEY
testnet_api_secret = "" # REPLACE WITH YOUR TESTNET API SECRET

default_leverage = 10  # Default leverage for placing orders
time_in_force = 'GoodTillCancel'

# --- Risk Management Parameters --- 
equity_risk_percent = 0.05  # Percentage of total equity to risk per trade (e.g., 0.01 = 1%)
price_stop_loss_percent = 0.02 # Default stop-loss percentage based on price for QTY calculation (e.g., 0.01 = 1%)

# --- Take Profit Settings --- 
enable_take_profit = True # Automatically add TP order? (True/False)
price_take_profit_percent = 0.04 # Price TP level (0.04 = 4%)

# --- Exit Strategy Settings --- 
enable_timed_exit = True # Automatically close position after a fixed time? (True)
                         # If False, position closes only when SL or TP is hit.
trade_cooldown_seconds = 11 

# Signal Keywords
keywords_long = ["bull", "bullish", "pump", "buy high sell higher", "long", "buy"]
keywords_short = ["bear", "bearish", "dump", "sell", "short"]

symbol_map = {
    '#btc': 'BTCUSDT',
    '$btc': 'BTCUSDT',
    'btc': 'BTCUSDT',
    'bitcoin': 'BTCUSDT',
    '#eth': 'ETHUSDT',
    '$eth': 'ETHUSDT',
    'eth': 'ETHUSDT',
    'ethereum': 'ETHUSDT',
    '#sol': 'SOLUSDT',
    '$sol': 'SOLUSDT',
    'sol': 'SOLUSDT',
    'solana': 'SOLUSDT',
    '#xrp': 'XRPUSDT',
    '$xrp': 'XRPUSDT',
    'xrp': 'XRPUSDT',
    'ripple': 'XRPUSDT',
    '#doge': 'DOGEUSDT',
    '$doge': 'DOGEUSDT',
    'doge': 'DOGEUSDT',
    'dogecoin': 'DOGEUSDT',
    '#ada': 'ADAUSDT',
    '$ada': 'ADAUSDT',
    'ada': 'ADAUSDT',
    'cardano': 'ADAUSDT',
    '#link': 'LINKUSDT',
    '$link': 'LINKUSDT',
    'link': 'LINKUSDT',
    'chainlink': 'LINKUSDT',
    '#matic': 'MATICUSDT',
    '$matic': 'MATICUSDT',
    'matic': 'MATICUSDT',
    'polygon': 'MATICUSDT', 
    '#avax': 'AVAXUSDT',
    '$avax': 'AVAXUSDT',
    'avax': 'AVAXUSDT',
    'avalanche': 'AVAXUSDT',
    '#dot': 'DOTUSDT',
    '$dot': 'DOTUSDT',
    'dot': 'DOTUSDT',
    'polkadot': 'DOTUSDT',
    '#ltc': 'LTCUSDT', # Eklendi
    '$ltc': 'LTCUSDT', # Eklendi
    'ltc': 'LTCUSDT',   # Eklendi
    'litecoin': 'LTCUSDT', # Eklendi
    '#bch': 'BCHUSDT', # Eklendi
    '$bch': 'BCHUSDT', # Eklendi
    'bch': 'BCHUSDT',   # Eklendi
    'bitcoincash': 'BCHUSDT', # Eklendi
    'bitcoin cash': 'BCHUSDT', # Eklendi
    '#bnb': 'BNBUSDT', # Eklendi
    '$bnb': 'BNBUSDT', # Eklendi
    'bnb': 'BNBUSDT',   # Eklendi
    'binancecoin': 'BNBUSDT', # Eklendi
    'binance coin': 'BNBUSDT', # Eklendi
    '#eos': 'EOSUSDT', # Eklendi
    '$eos': 'EOSUSDT', # Eklendi
    'eos': 'EOSUSDT',   # Eklendi
    '#xlm': 'XLMUSDT', # Eklendi
    '$xlm': 'XLMUSDT', # Eklendi
    'xlm': 'XLMUSDT',   # Eklendi
    'stellar': 'XLMUSDT', # Eklendi
    'stellar lumens': 'XLMUSDT', # Eklendi
    '#xmr': 'XMRUSDT', # Eklendi
    '$xmr': 'XMRUSDT', # Eklendi
    'xmr': 'XMRUSDT',   # Eklendi
    'monero': 'XMRUSDT', # Eklendi
    '#trx': 'TRXUSDT', # Eklendi
    '$trx': 'TRXUSDT', # Eklendi
    'trx': 'TRXUSDT',   # Eklendi
    'tron': 'TRXUSDT',  # Eklendi
    '#etc': 'ETCUSDT', # Eklendi
    '$etc': 'ETCUSDT', # Eklendi
    'etc': 'ETCUSDT',   # Eklendi
    'ethereumclassic': 'ETCUSDT', # Eklendi
    'ethereum classic': 'ETCUSDT', # Eklendi
    '#atom': 'ATOMUSDT', # Eklendi
    '$atom': 'ATOMUSDT', # Eklendi
    'atom': 'ATOMUSDT',  # Eklendi
    'cosmos': 'ATOMUSDT', # Eklendi
    '#xtz': 'XTZUSDT', # Eklendi
    '$xtz': 'XTZUSDT', # Eklendi
    'xtz': 'XTZUSDT',   # Eklendi
    'tezos': 'XTZUSDT', # Eklendi
    '#near': 'NEARUSDT', # Eklendi
    '$near': 'NEARUSDT', # Eklendi
    'near': 'NEARUSDT',  # Eklendi
    'nearprotocol': 'NEARUSDT', # Eklendi
    'near protocol': 'NEARUSDT', # Eklendi
    '#fil': 'FILUSDT', # Eklendi
    '$fil': 'FILUSDT', # Eklendi
    'fil': 'FILUSDT',   # Eklendi
    'filecoin': 'FILUSDT', # Eklendi
    '#uni': 'UNIUSDT', # Eklendi
    '$uni': 'UNIUSDT', # Eklendi
    'uni': 'UNIUSDT',   # Eklendi
    'uniswap': 'UNIUSDT', # Eklendi
    '#icp': 'ICPUSDT', # Eklendi
    '$icp': 'ICPUSDT', # Eklendi
    'icp': 'ICPUSDT',   # Eklendi
    'internetcomputer': 'ICPUSDT', # Eklendi
    'internet computer': 'ICPUSDT', # Eklendi
    '#aave': 'AAVEUSDT', # Eklendi
    '$aave': 'AAVEUSDT', # Eklendi
    'aave': 'AAVEUSDT',  # Eklendi (Popülerlerde vardı, buraya da taşıdım)
    '#grt': 'GRTUSDT', # Eklendi
    '$grt': 'GRTUSDT', # Eklendi
    'grt': 'GRTUSDT',   # Eklendi
    'thegraph': 'GRTUSDT', # Eklendi
    'the graph': 'GRTUSDT', # Eklendi
    '#mkr': 'MKRUSDT', # Eklendi
    '$mkr': 'MKRUSDT', # Eklendi
    'mkr': 'MKRUSDT',   # Eklendi
    'maker': 'MKRUSDT', # Eklendi
    '#algo': 'ALGOUSDT', # Eklendi
    '$algo': 'ALGOUSDT', # Eklendi
    'algo': 'ALGOUSDT',  # Eklendi
    'algorand': 'ALGOUSDT', # Eklendi
    '#sand': 'SANDUSDT', # Eklendi
    '$sand': 'SANDUSDT', # Eklendi
    'sand': 'SANDUSDT',  # Eklendi
    'sandbox': 'SANDUSDT',# Eklendi
    'the sandbox': 'SANDUSDT', # Eklendi
    '#mana': 'MANAUSDT', # Eklendi
    '$mana': 'MANAUSDT', # Eklendi
    'mana': 'MANAUSDT',  # Eklendi
    'decentraland': 'MANAUSDT', # Eklendi
    '#axs': 'AXSUSDT', # Eklendi
    '$axs': 'AXSUSDT', # Eklendi
    'axs': 'AXSUSDT',   # Eklendi
    'axie': 'AXSUSDT', # Eklendi
    'axieinfinity': 'AXSUSDT', # Eklendi
    'axie infinity': 'AXSUSDT', # Eklendi
    '#egld': 'EGLDUSDT', # Eklendi
    '$egld': 'EGLDUSDT', # Eklendi
    'egld': 'EGLDUSDT',  # Eklendi
    'elrond': 'EGLDUSDT', # Eski adı, hala kullanılabilir
    'multiversx': 'EGLDUSDT', # Yeni adı

    # --- Özel veya Standart Dışı İsimler (Mevcut Örnekler ve Eklemeler) ---
    '#aidoge': '10000000AIDOGEUSDT', # Bu özel kalacak
    '$aidoge': '10000000AIDOGEUSDT',
    'aidoge': '10000000AIDOGEUSDT',
    'arbidooge': '10000000AIDOGEUSDT', # Olası alternatif
    '#coq': '10000COQUSDT',
    '$coq': '10000COQUSDT',
    'coq': '10000COQUSDT',
    'coqinu': '10000COQUSDT', # Olası alternatif
    '#ladys': '10000LADYSUSDT',
    '$ladys': '10000LADYSUSDT',
    'ladys': '10000LADYSUSDT',
    'milady': '10000LADYSUSDT', # Olası alternatif
    '#nft': '10000NFTUSDT', # Bu özel kalacak
    '$nft': '10000NFTUSDT',
    'nft': '10000NFTUSDT',
    'apenft': '10000NFTUSDT', # Olası alternatif
    '#sats': '10000SATSUSDT',
    '$sats': '10000SATSUSDT',
    'sats': '10000SATSUSDT', # BRC-20 token
    '#starl': '10000STARLUSDT',
    '$starl': '10000STARLUSDT',
    'starl': '10000STARLUSDT',
    'starlink': '10000STARLUSDT', # Olası alternatif
    '#wen': '10000WENUSDT',
    '$wen': '10000WENUSDT',
    'wen': '10000WENUSDT',
    '#bonk': '1000BONKUSDT',
    '$bonk': '1000BONKUSDT',
    'bonk': '1000BONKUSDT',
    'bonkinu': '1000BONKUSDT', # Olası
    '#btt': '1000BTTUSDT',
    '$btt': '1000BTTUSDT',
    'btt': '1000BTTUSDT',
    'bittorrent': '1000BTTUSDT',
    '#floki': '1000FLOKIUSDT',
    '$floki': '1000FLOKIUSDT',
    'floki': '1000FLOKIUSDT',
    'flokiinu': '1000FLOKIUSDT',
    'floki inu': '1000FLOKIUSDT',
    '#iq50': '1000IQ50USDT',
    '$iq50': '1000IQ50USDT',
    'iq50': '1000IQ50USDT',
    '#lunc': '1000LUNCUSDT',
    '$lunc': '1000LUNCUSDT',
    'lunc': '1000LUNCUSDT',
    'terraclassic': '1000LUNCUSDT',
    'terra classic': '1000LUNCUSDT',
    'lunaclassic': '1000LUNCUSDT',
    'luna classic': '1000LUNCUSDT',
    '#pepe': '1000PEPEUSDT',
    '$pepe': '1000PEPEUSDT',
    'pepe': '1000PEPEUSDT',
    'pepecoin': '1000PEPEUSDT',
    'frogcoin': '1000PEPEUSDT', # Çok yaygın değil ama bazen
    '#rats': '1000RATSUSDT',
    '$rats': '1000RATSUSDT',
    'rats': '1000RATSUSDT', # BRC-20 token
    '#turbo': '1000TURBOUSDT',
    '$turbo': '1000TURBOUSDT',
    'turbo': '1000TURBOUSDT',
    '#xec': '1000XECUSDT',
    '$xec': '1000XECUSDT',
    'xec': '1000XECUSDT',
    'ecash': '1000XECUSDT',
    'e-cash': '1000XECUSDT',
    '#shib': 'SHIB1000USDT', # SHIB1000USDT için
    '$shib': 'SHIB1000USDT',
    'shib': 'SHIB1000USDT',
    'shibainu': 'SHIB1000USDT',
    'shiba inu': 'SHIB1000USDT',
    'shib1000': 'SHIB1000USDT', # Zaten vardı, teyit
    '$shib1000': 'SHIB1000USDT',
    '#shib1000': 'SHIB1000USDT',

    # --- Yeni Eklenenler (Otomatik Oluşturuldu ve Bazı Alternatifler Eklendi) ---
    '#gmx': 'GMXUSDT',
    '$gmx': 'GMXUSDT',
    'gmx': 'GMXUSDT',
    '#rlc': 'RLCUSDT',
    '$rlc': 'RLCUSDT',
    'rlc': 'RLCUSDT',
    'iexecrlc': 'RLCUSDT',
    'iexec rlc': 'RLCUSDT',
    '#goatusdt': 'GOATUSDT', # GOATUSDT -> goatusdt (Alternatif zor)
    '$goatusdt': 'GOATUSDT',
    'goatusdt': 'GOATUSDT',
    '#myria': 'MYRIAUSDT',
    '$myria': 'MYRIAUSDT',
    'myria': 'MYRIAUSDT',
    '#pump': 'PUMPUSDT',
    '$pump': 'PUMPUSDT',
    'pump': 'PUMPUSDT',
    '#bico': 'BICOUSDT',
    '$bico': 'BICOUSDT',
    'bico': 'BICOUSDT',
    'biconomy': 'BICOUSDT',
    '#xch': 'XCHUSDT',
    '$xch': 'XCHUSDT',
    'xch': 'XCHUSDT',
    'chia': 'XCHUSDT',
    '#cookie': 'COOKIEUSDT',
    '$cookie': 'COOKIEUSDT',
    'cookie': 'COOKIEUSDT',
    '#usdc': 'USDCUSDT',
    '$usdc': 'USDCUSDT',
    'usdc': 'USDCUSDT',
    'usdcoin': 'USDCUSDT',
    'usd coin': 'USDCUSDT',
    '#zro': 'ZROUSDT',
    '$zro': 'ZROUSDT',
    'zro': 'ZROUSDT',
    'layerzero': 'ZROUSDT',
    'layer zero': 'ZROUSDT',
    '#ata': 'ATAUSDT',
    '$ata': 'ATAUSDT',
    'ata': 'ATAUSDT',
    'automata': 'ATAUSDT',
    '#celr': 'CELRUSDT',
    '$celr': 'CELRUSDT',
    'celr': 'CELRUSDT',
    'celer': 'CELRUSDT',
    'celer network': 'CELRUSDT',
    '#people': 'PEOPLEUSDT',
    '$people': 'PEOPLEUSDT',
    'people': 'PEOPLEUSDT',
    'constitutiondao': 'PEOPLEUSDT',
    'constitution dao': 'PEOPLEUSDT',
    '#arpa': 'ARPAUSDT',
    '$arpa': 'ARPAUSDT',
    'arpa': 'ARPAUSDT',
    'arpachain': 'ARPAUSDT',
    'arpa chain': 'ARPAUSDT',
    '#nil': 'NILUSDT',
    '$nil': 'NILUSDT',
    'nil': 'NILUSDT',
    '#dash': 'DASHUSDT', # Popülerlerde vardı, burada da olsun
    '$dash': 'DASHUSDT',
    'dash': 'DASHUSDT',
    '#imx': 'IMXUSDT',
    '$imx': 'IMXUSDT',
    'imx': 'IMXUSDT',
    'immutable': 'IMXUSDT',
    'immutablex': 'IMXUSDT',
    'immutable x': 'IMXUSDT',
    '#ssv': 'SSVUSDT',
    '$ssv': 'SSVUSDT',
    'ssv': 'SSVUSDT',
    'ssvnetwork': 'SSVUSDT',
    'ssv network': 'SSVUSDT',
    '#flr': 'FLRUSDT',
    '$flr': 'FLRUSDT',
    'flr': 'FLRUSDT',
    'flare': 'FLRUSDT',
    'flarenetwork': 'FLRUSDT',
    'flare network': 'FLRUSDT',
    '#hpos10i': 'HPOS10IUSDT', # HPOS10IUSDT -> hpos10i (Alternatif zor)
    '$hpos10i': 'HPOS10IUSDT',
    'hpos10i': 'HPOS10IUSDT',
    '#strk': 'STRKUSDT',
    '$strk': 'STRKUSDT',
    'strk': 'STRKUSDT',
    'starknet': 'STRKUSDT',
    '#omg': 'OMGUSDT',
    '$omg': 'OMGUSDT',
    'omg': 'OMGUSDT',
    'omgnetwork': 'OMGUSDT',
    'omg network': 'OMGUSDT', # Eskiden OmiseGO
    'omisego': 'OMGUSDT',
    '#hot': 'HOTUSDT',
    '$hot': 'HOTUSDT',
    'hot': 'HOTUSDT',
    'holo': 'HOTUSDT',
    'holochain': 'HOTUSDT',
    '#alpha': 'ALPHAUSDT',
    '$alpha': 'ALPHAUSDT',
    'alpha': 'ALPHAUSDT',
    'stellarlumens': 'ALPHAUSDT', # Alpha Finance Lab, Stella ile birleşti sanırım? Ya da kendi adı.
    'alphafinance': 'ALPHAUSDT',
    '#op': 'OPUSDT',
    '$op': 'OPUSDT',
    'op': 'OPUSDT',
    'optimism': 'OPUSDT',
    '#nc': 'NCUSDT', # Alternatif zor
    '$nc': 'NCUSDT',
    'nc': 'NCUSDT',
    '#storj': 'STORJUSDT',
    '$storj': 'STORJUSDT',
    'storj': 'STORJUSDT',
    '#usde': 'USDEUSDT',
    '$usde': 'USDEUSDT',
    'usde': 'USDEUSDT',
    'ethena usde': 'USDEUSDT', # Ethena'nın stablecoin'i
    '#yfi': 'YFIUSDT',
    '$yfi': 'YFIUSDT',
    'yfi': 'YFIUSDT',
    'yearn': 'YFIUSDT',
    'yearnfinance': 'YFIUSDT',
    'yearn finance': 'YFIUSDT',
    '#fio': 'FIOUSDT',
    '$fio': 'FIOUSDT',
    'fio': 'FIOUSDT',
    'fioprotocol': 'FIOUSDT',
    'fio protocol': 'FIOUSDT',
    '#ach': 'ACHUSDT',
    '$ach': 'ACHUSDT',
    'ach': 'ACHUSDT',
    'alchemy': 'ACHUSDT', # Alchemy Pay
    'alchemypay': 'ACHUSDT',
    'alchemy pay': 'ACHUSDT',
    '#mavia': 'MAVIAUSDT',
    '$mavia': 'MAVIAUSDT',
    'mavia': 'MAVIAUSDT',
    'heroesofmavia': 'MAVIAUSDT',
    'heroes of mavia': 'MAVIAUSDT',
    '#ctk': 'CTKUSDT',
    '$ctk': 'CTKUSDT',
    'ctk': 'CTKUSDT',
    'certik': 'CTKUSDT',
    '#bio': 'BIOUSDT', # Alternatif zor
    '$bio': 'BIOUSDT',
    'bio': 'BIOUSDT',
    '#s': 'SUSDT', # SUSDT -> s (Synthetix USD - sUSD)
    '$s': 'SUSDT',
    's': 'SUSDT',
    'susd': 'SUSDT',
    '#act': 'ACTUSDT',
    '$act': 'ACTUSDT',
    'act': 'ACTUSDT',
    'aelf': 'ACTUSDT', # Eğer bu Achain ise (ACT), Aelf (ELF) ile karışmamalı. ACT için zor.
    '#pyth': 'PYTHUSDT',
    '$pyth': 'PYTHUSDT',
    'pyth': 'PYTHUSDT',
    'pythnetwork': 'PYTHUSDT',
    'pyth network': 'PYTHUSDT',
    '#moca': 'MOCAUSDT',
    '$moca': 'MOCAUSDT',
    'moca': 'MOCAUSDT',
    'mocaverse': 'MOCAUSDT',
    '#bnt': 'BNTUSDT',
    '$bnt': 'BNTUSDT',
    'bnt': 'BNTUSDT',
    'bancor': 'BNTUSDT',
    '#manta': 'MANTAUSDT',
    '$manta': 'MANTAUSDT',
    'manta': 'MANTAUSDT',
    'mantanetwork': 'MANTAUSDT',
    'manta network': 'MANTAUSDT',
    '#init': 'INITUSDT', # Alternatif zor
    '$init': 'INITUSDT',
    'init': 'INITUSDT',
    '#ordi': 'ORDIUSDT',
    '$ordi': 'ORDIUSDT',
    'ordi': 'ORDIUSDT', # BRC-20
    'ordinals': 'ORDIUSDT', # Bazen
    '#gmt': 'GMTUSDT',
    '$gmt': 'GMTUSDT',
    'gmt': 'GMTUSDT',
    'stepn': 'GMTUSDT',
    '#req': 'REQUSDT',
    '$req': 'REQUSDT',
    'req': 'REQUSDT',
    'request': 'REQUSDT',
    'requestnetwork': 'REQUSDT',
    'request network': 'REQUSDT',
    '#band': 'BANDUSDT',
    '$band': 'BANDUSDT',
    'band': 'BANDUSDT',
    'bandprotocol': 'BANDUSDT',
    'band protocol': 'BANDUSDT',
    '#ar': 'ARUSDT',
    '$ar': 'ARUSDT',
    'ar': 'ARUSDT',
    'arweave': 'ARUSDT',
    '#cetus': 'CETUSUSDT',
    '$cetus': 'CETUSUSDT',
    'cetus': 'CETUSUSDT',
    'cetusprotocol': 'CETUSUSDT',
    'cetus protocol': 'CETUSUSDT',
    '#g': 'GUSDT', # GRT's G? Zor.
    '$g': 'GUSDT',
    'g': 'GUSDT',
    '#cpool': 'CPOOLUSDT',
    '$cpool': 'CPOOLUSDT',
    'cpool': 'CPOOLUSDT',
    'clearpool': 'CPOOLUSDT',
    '#hook': 'HOOKUSDT',
    '$hook': 'HOOKUSDT',
    'hook': 'HOOKUSDT',
    'hookedprotocol': 'HOOKUSDT',
    'hooked protocol': 'HOOKUSDT',
    '#sui': 'SUIUSDT',
    '$sui': 'SUIUSDT',
    'sui': 'SUIUSDT',
    'suinetwork': 'SUIUSDT', # Bazen
    '#usual': 'USUALUSDT', # Alternatif zor
    '$usual': 'USUALUSDT',
    'usual': 'USUALUSDT',
    '#w': 'WUSDT', # Wormhole?
    '$w': 'WUSDT',
    'w': 'WUSDT',
    'wormhole': 'WUSDT', # Eğer buysa
    '#lsk': 'LSKUSDT',
    '$lsk': 'LSKUSDT',
    'lsk': 'LSKUSDT',
    'lisk': 'LSKUSDT',
    '#cow': 'COWUSDT',
    '$cow': 'COWUSDT',
    'cow': 'COWUSDT',
    'cowswap': 'COWUSDT',
    'cow protocol': 'COWUSDT',
    '#sfp': 'SFPUSDT',
    '$sfp': 'SFPUSDT',
    'sfp': 'SFPUSDT',
    'safepal': 'SFPUSDT',
    '#ai': 'AIUSDT',
    '$ai': 'AIUSDT',
    'ai': 'AIUSDT',
    'sleeplessai': 'AIUSDT', # Eğer buysa
    'sleepless ai': 'AIUSDT',
    '#gtc': 'GTCUSDT',
    '$gtc': 'GTCUSDT',
    'gtc': 'GTCUSDT',
    'gitcoin': 'GTCUSDT',
    '#pha': 'PHAUSDT',
    '$pha': 'PHAUSDT',
    'pha': 'PHAUSDT',
    'phala': 'PHAUSDT',
    'phalanetwork': 'PHAUSDT',
    'phala network': 'PHAUSDT',
    '#foxy': 'FOXYUSDT', # Alternatif zor
    '$foxy': 'FOXYUSDT',
    'foxy': 'FOXYUSDT',
    '#gork': 'GORKUSDT', # Alternatif zor
    '$gork': 'GORKUSDT',
    'gork': 'GORKUSDT',
    '#haedal': 'HAEDALUSDT', # Alternatif zor
    '$haedal': 'HAEDALUSDT',
    'haedal': 'HAEDALUSDT',
    '#hbar': 'HBARUSDT',
    '$hbar': 'HBARUSDT',
    'hbar': 'HBARUSDT',
    'hedera': 'HBARUSDT',
    'hederahashgraph': 'HBARUSDT',
    'hedera hashgraph': 'HBARUSDT',
    '#icx': 'ICXUSDT',
    '$icx': 'ICXUSDT',
    'icx': 'ICXUSDT',
    'icon': 'ICXUSDT',
    '#pixel': 'PIXELUSDT',
    '$pixel': 'PIXELUSDT',
    'pixel': 'PIXELUSDT',
    'pixels': 'PIXELUSDT',
    '#vr': 'VRUSDT',
    '$vr': 'VRUSDT',
    'vr': 'VRUSDT',
    'victoriavr': 'VRUSDT',
    'victoria vr': 'VRUSDT',
    '#idex': 'IDEXUSDT',
    '$idex': 'IDEXUSDT',
    'idex': 'IDEXUSDT',
    '#solv': 'SOLVUSDT',
    '$solv': 'SOLVUSDT',
    'solv': 'SOLVUSDT',
    'solvprotocol': 'SOLVUSDT',
    'solv protocol': 'SOLVUSDT',
    '#roam': 'ROAMUSDT', # Alternatif zor
    '$roam': 'ROAMUSDT',
    'roam': 'ROAMUSDT',
    '#gno': 'GNOUSDT',
    '$gno': 'GNOUSDT',
    'gno': 'GNOUSDT',
    'gnosis': 'GNOUSDT',
    '#dusk': 'DUSKUSDT',
    '$dusk': 'DUSKUSDT',
    'dusk': 'DUSKUSDT',
    'dusknetwork': 'DUSKUSDT',
    'dusk network': 'DUSKUSDT',
    '#raydium': 'RAYDIUMUSDT', # Zaten tam adı
    '$raydium': 'RAYDIUMUSDT',
    'raydium': 'RAYDIUMUSDT',
    'ray': 'RAYDIUMUSDT', # Kısa hali
    '#dark': 'DARKUSDT', # Alternatif zor
    '$dark': 'DARKUSDT',
    'dark': 'DARKUSDT',
    '#rune': 'RUNEUSDT',
    '$rune': 'RUNEUSDT',
    'rune': 'RUNEUSDT',
    'thorchain': 'RUNEUSDT',
    '#aleo': 'ALEOUSDT', # Alternatif zor
    '$aleo': 'ALEOUSDT',
    'aleo': 'ALEOUSDT',
    '#shell': 'SHELLUSDT', # Alternatif zor
    '$shell': 'SHELLUSDT',
    'shell': 'SHELLUSDT',
    '#babydoge': '1000000BABYDOGEUSDT', # Popülerlerde vardı, burada da olsun
    '$babydoge': '1000000BABYDOGEUSDT',
    'babydoge': '1000000BABYDOGEUSDT',
    'babydogecoin': '1000000BABYDOGEUSDT',
    'baby doge': '1000000BABYDOGEUSDT',
    '#rfc': 'RFCUSDT', # Alternatif zor
    '$rfc': 'RFCUSDT',
    'rfc': 'RFCUSDT',
    '#slp': 'SLPUSDT',
    '$slp': 'SLPUSDT',
    'slp': 'SLPUSDT',
    'smoothlovepotion': 'SLPUSDT',
    'smooth love potion': 'SLPUSDT',
    '#neiroeth': 'NEIROETHUSDT', # Alternatif zor
    '$neiroeth': 'NEIROETHUSDT',
    'neiroeth': 'NEIROETHUSDT',
    '#oxt': 'OXTUSDT',
    '$oxt': 'OXTUSDT',
    'oxt': 'OXTUSDT',
    'orchid': 'OXTUSDT',
    '#tstbsc': 'TSTBSCUSDT', # Test token, alternatif yok
    '$tstbsc': 'TSTBSCUSDT',
    'tstbsc': 'TSTBSCUSDT',
    '#b3': 'B3USDT', # Alternatif zor
    '$b3': 'B3USDT',
    'b3': 'B3USDT',
    '#ogn': 'OGNUSDT',
    '$ogn': 'OGNUSDT',
    'ogn': 'OGNUSDT',
    'origin': 'OGNUSDT',
    'originprotocol': 'OGNUSDT',
    'origin protocol': 'OGNUSDT',
    '#ong': 'ONGUSDT',
    '$ong': 'ONGUSDT',
    'ong': 'ONGUSDT',
    'ontologygas': 'ONGUSDT',
    'ontology gas': 'ONGUSDT',
    '#zen': 'ZENUSDT',
    '$zen': 'ZENUSDT',
    'zen': 'ZENUSDT',
    'horizen': 'ZENUSDT',
    '#hype': 'HYPEUSDT', # Alternatif zor
    '$hype': 'HYPEUSDT',
    'hype': 'HYPEUSDT',
    '#swarms': 'SWARMSUSDT', # Alternatif zor
    '$swarms': 'SWARMSUSDT',
    'swarms': 'SWARMSUSDT',
    '#axl': 'AXLUSDT',
    '$axl': 'AXLUSDT',
    'axl': 'AXLUSDT',
    'axelar': 'AXLUSDT',
    '#catiusdt': 'CATIUSDT', # CATIUSDT -> catiusdt (Alternatif zor)
    '$catiusdt': 'CATIUSDT',
    'catiusdt': 'CATIUSDT',
    '#vra': 'VRAUSDT',
    '$vra': 'VRAUSDT',
    'vra': 'VRAUSDT',
    'verasity': 'VRAUSDT',
    '#ava': 'AVAUSDT',
    '$ava': 'AVAUSDT',
    'ava': 'AVAUSDT',
    'travala': 'AVAUSDT',
    '#mbl': 'MBLUSDT',
    '$mbl': 'MBLUSDT',
    'mbl': 'MBLUSDT',
    'moviebloc': 'MBLUSDT',
    '#og': 'OGUSDT',
    '$og': 'OGUSDT',
    'og': 'OGUSDT',
    'ogfans': 'OGUSDT', # OG Fan Token
    'og fan token': 'OGUSDT',
    '#nkn': 'NKNUSDT',
    '$nkn': 'NKNUSDT',
    'nkn': 'NKNUSDT',
    'newkindofnetwork': 'NKNUSDT',
    'new kind of network': 'NKNUSDT',
    '#waves': 'WAVESUSDT',
    '$waves': 'WAVESUSDT',
    'waves': 'WAVESUSDT',
    '#fhe': 'FHEUSDT', # Alternatif zor
    '$fhe': 'FHEUSDT',
    'fhe': 'FHEUSDT',
    '#forth': 'FORTHUSDT',
    '$forth': 'FORTHUSDT',
    'forth': 'FORTHUSDT',
    'ampleforthgovernance': 'FORTHUSDT',
    'ampleforth governance token': 'FORTHUSDT',
    '#cook': 'COOKUSDT', # Alternatif zor
    '$cook': 'COOKUSDT',
    'cook': 'COOKUSDT',
    'cookprotocol': 'COOKUSDT',
    '#clanker': 'CLANKERUSDT', # Alternatif zor
    '$clanker': 'CLANKERUSDT',
    'clanker': 'CLANKERUSDT',
    '#orbs': 'ORBSUSDT',
    '$orbs': 'ORBSUSDT',
    'orbs': 'ORBSUSDT',
    '#avail': 'AVAILUSDT', # Alternatif zor
    '$avail': 'AVAILUSDT',
    'avail': 'AVAILUSDT',
    '#skl': 'SKLUSDT',
    '$skl': 'SKLUSDT',
    'skl': 'SKLUSDT',
    'skale': 'SKLUSDT',
    'skalenetwork': 'SKLUSDT',
    'skale network': 'SKLUSDT',
    '#morpho': 'MORPHOUSDT', # Alternatif zor
    '$morpho': 'MORPHOUSDT',
    'morpho': 'MORPHOUSDT',
    '#neo': 'NEOUSDT', # Popülerlerde vardı
    '$neo': 'NEOUSDT',
    'neo': 'NEOUSDT',
    '#rdnt': 'RDNTUSDT',
    '$rdnt': 'RDNTUSDT',
    'rdnt': 'RDNTUSDT',
    'radiant': 'RDNTUSDT',
    'radiantcapital': 'RDNTUSDT',
    'radiant capital': 'RDNTUSDT',
    '#comp': 'COMPUSDT',
    '$comp': 'COMPUSDT',
    'comp': 'COMPUSDT',
    'compound': 'COMPUSDT',
    '#magic': 'MAGICUSDT',
    '$magic': 'MAGICUSDT',
    'magic': 'MAGICUSDT', # Treasure
    '#peaq': 'PEAQUSDT', # Alternatif zor
    '$peaq': 'PEAQUSDT',
    'peaq': 'PEAQUSDT',
    '#pyr': 'PYRUSDT',
    '$pyr': 'PYRUSDT',
    'pyr': 'PYRUSDT',
    'vulcanforged': 'PYRUSDT',
    'vulcan forged': 'PYRUSDT',
    '#prompt': 'PROMPTUSDT', # Alternatif zor
    '$prompt': 'PROMPTUSDT',
    'prompt': 'PROMPTUSDT',
    '#arc': 'ARCUSDT', # Alternatif zor
    '$arc': 'ARCUSDT',
    'arc': 'ARCUSDT',
    '#stg': 'STGUSDT',
    '$stg': 'STGUSDT',
    'stg': 'STGUSDT',
    'stargate': 'STGUSDT',
    'stargatefinance': 'STGUSDT',
    'stargate finance': 'STGUSDT',
    '#elx': 'ELXUSDT', # Alternatif zor
    '$elx': 'ELXUSDT',
    'elx': 'ELXUSDT',
    '#cloud': 'CLOUDUSDT', # Alternatif zor
    '$cloud': 'CLOUDUSDT',
    'cloud': 'CLOUDUSDT',
    '#ape': 'APEUSDT',
    '$ape': 'APEUSDT',
    'ape': 'APEUSDT',
    'apecoin': 'APEUSDT',
    '#scrt': 'SCRTUSDT',
    '$scrt': 'SCRTUSDT',
    'scrt': 'SCRTUSDT',
    'secret': 'SCRTUSDT',
    'secretnetwork': 'SCRTUSDT',
    'secret network': 'SCRTUSDT',
    '#gala': 'GALAUSDT',
    '$gala': 'GALAUSDT',
    'gala': 'GALAUSDT',
    'galagames': 'GALAUSDT',
    'gala games': 'GALAUSDT',
    '#xrd': 'XRDUSDT',
    '$xrd': 'XRDUSDT',
    'xrd': 'XRDUSDT',
    'radix': 'XRDUSDT',
    '#the': 'THEUSDT', # Alternatif zor
    '$the': 'THEUSDT',
    'the': 'THEUSDT',
    '#dog': 'DOGUSDT', # DOGUSDT -> dog (doge değil!)
    '$dog': 'DOGUSDT',
    'dog': 'DOGUSDT',
    'thedog': 'DOGUSDT', # Belki, "Dog (Runes)"
    '#melania': 'MELANIAUSDT', # Alternatif zor
    '$melania': 'MELANIAUSDT',
    'melania': 'MELANIAUSDT',
    '#jasmy': 'JASMYUSDT',
    '$jasmy': 'JASMYUSDT',
    'jasmy': 'JASMYUSDT',
    'jasmycoin': 'JASMYUSDT',
    '#blast': 'BLASTUSDT', # Alternatif zor
    '$blast': 'BLASTUSDT',
    'blast': 'BLASTUSDT',
    '#trb': 'TRBUSDT',
    '$trb': 'TRBUSDT',
    'trb': 'TRBUSDT',
    'tellor': 'TRBUSDT',
    '#dbr': 'DBRUSDT', # Alternatif zor
    '$dbr': 'DBRUSDT',
    'dbr': 'DBRUSDT',
    '#giga': 'GIGAUSDT', # Alternatif zor
    '$giga': 'GIGAUSDT',
    'giga': 'GIGAUSDT',
    '#cro': 'CROUSDT',
    '$cro': 'CROUSDT',
    'cro': 'CROUSDT',
    'cronos': 'CROUSDT',
    'cryptocom': 'CROUSDT',
    'crypto.com': 'CROUSDT',
    'crypto com': 'CROUSDT',
    '#ctc': 'CTCUSDT',
    '$ctc': 'CTCUSDT',
    'ctc': 'CTCUSDT',
    'creditcoin': 'CTCUSDT',
    '#t': 'TUSDT', # Threshold Network Token
    '$t': 'TUSDT',
    't': 'TUSDT',
    'threshold': 'TUSDT',
    'thresholdnetwork': 'TUSDT',
    '#pundix': 'PUNDIXUSDT', # Zaten tam adı
    '$pundix': 'PUNDIXUSDT',
    'pundix': 'PUNDIXUSDT',
    '#ath': 'ATHUSDT', # Alternatif zor
    '$ath': 'ATHUSDT',
    'ath': 'ATHUSDT',
    '#glm': 'GLMUSDT',
    '$glm': 'GLMUSDT',
    'glm': 'GLMUSDT',
    'golem': 'GLMUSDT',
    '#rif': 'RIFUSDT',
    '$rif': 'RIFUSDT',
    'rif': 'RIFUSDT',
    'rsk': 'RIFUSDT', # RSK Infrastructure Framework
    'rskinfrastructure': 'RIFUSDT',
    '#fxs': 'FXSUSDT',
    '$fxs': 'FXSUSDT',
    'fxs': 'FXSUSDT',
    'frax': 'FXSUSDT',
    'fraxshare': 'FXSUSDT',
    'frax share': 'FXSUSDT',
    '#ton': 'TONUSDT',
    '$ton': 'TONUSDT',
    'ton': 'TONUSDT',
    'toncoin': 'TONUSDT',
    'theopennetwork': 'TONUSDT',
    'the open network': 'TONUSDT',
    '#cyber': 'CYBERUSDT',
    '$cyber': 'CYBERUSDT',
    'cyber': 'CYBERUSDT',
    'cyberconnect': 'CYBERUSDT',
    '#epic': 'EPICUSDT', # Alternatif zor
    '$epic': 'EPICUSDT',
    'epic': 'EPICUSDT',
    '#eigen': 'EIGENUSDT',
    '$eigen': 'EIGENUSDT',
    'eigen': 'EIGENUSDT',
    'eigenlayer': 'EIGENUSDT',
    '#sd': 'SDUSDT',
    '$sd': 'SDUSDT',
    'sd': 'SDUSDT',
    'stader': 'SDUSDT',
    '#mav': 'MAVUSDT',
    '$mav': 'MAVUSDT',
    'mav': 'MAVUSDT',
    'maverick': 'MAVUSDT',
    'maverickprotocol': 'MAVUSDT',
    'maverick protocol': 'MAVUSDT',
    '#moodeng': 'MOODENGUSDT', # Alternatif zor
    '$moodeng': 'MOODENGUSDT',
    'moodeng': 'MOODENGUSDT',
    '#snt': 'SNTUSDT',
    '$snt': 'SNTUSDT',
    'snt': 'SNTUSDT',
    'status': 'SNTUSDT',
    '#j': 'JUSDT', # Joltify? Zor.
    '$j': 'JUSDT',
    'j': 'JUSDT',
    '#elon': '10000ELONUSDT', # Dogelon Mars
    '$elon': '10000ELONUSDT',
    'elon': '10000ELONUSDT',
    'dogelon': '10000ELONUSDT',
    'dogelonmars': '10000ELONUSDT',
    'dogelon mars': '10000ELONUSDT',
    '#xaut': 'XAUTUSDT', # Tether Gold
    '$xaut': 'XAUTUSDT',
    'xaut': 'XAUTUSDT',
    'tethergold': 'XAUTUSDT',
    'tether gold': 'XAUTUSDT',
    '#sundog': 'SUNDOGUSDT', # Alternatif zor
    '$sundog': 'SUNDOGUSDT',
    'sundog': 'SUNDOGUSDT',
    '#zkj': 'ZKJUSDT', # Alternatif zor
    '$zkj': 'ZKJUSDT',
    'zkj': 'ZKJUSDT',
    '#mubarak': 'MUBARAKUSDT', # Alternatif zor
    '$mubarak': 'MUBARAKUSDT',
    'mubarak': 'MUBARAKUSDT',
    '#zrc': 'ZRCUSDT', # Alternatif zor
    '$zrc': 'ZRCUSDT',
    'zrc': 'ZRCUSDT',
    '#koma': 'KOMAUSDT', # Alternatif zor
    '$koma': 'KOMAUSDT',
    'koma': 'KOMAUSDT',
    '#iost': 'IOSTUSDT',
    '$iost': 'IOSTUSDT',
    'iost': 'IOSTUSDT',
    '#syn': 'SYNUSDT',
    '$syn': 'SYNUSDT',
    'syn': 'SYNUSDT',
    'synapse': 'SYNUSDT',
    '#sto': 'STOUSDT', # Alternatif zor
    '$sto': 'STOUSDT',
    'sto': 'STOUSDT',
    '#metis': 'METISUSDT', # Zaten tam adı
    '$metis': 'METISUSDT',
    'metis': 'METISUSDT',
    '#zk': 'ZKUSDT',
    '$zk': 'ZKUSDT',
    'zk': 'ZKUSDT',
    'zksync': 'ZKUSDT', # Polyhedra (ZK) ile karışabilir, dikkat
    'polyhedra': 'ZKUSDT', # Eğer bu Polyhedra ise
    '#zrx': 'ZRXUSDT',
    '$zrx': 'ZRXUSDT',
    'zrx': 'ZRXUSDT',
    '0x': 'ZRXUSDT',
    'zerox': 'ZRXUSDT',
    '#sun': 'SUNUSDT', # TRON'un SUN'u
    '$sun': 'SUNUSDT',
    'sun': 'SUNUSDT',
    '#ckb': 'CKBUSDT',
    '$ckb': 'CKBUSDT',
    'ckb': 'CKBUSDT',
    'nervos': 'CKBUSDT',
    'nervosnetwork': 'CKBUSDT',
    'nervos network': 'CKBUSDT',
    '#ol': 'OLUSDT', # Alternatif zor
    '$ol': 'OLUSDT',
    'ol': 'OLUSDT',
    '#baby': 'BABYUSDT', # Alternatif zor (BabySwap?)
    '$baby': 'BABYUSDT',
    'baby': 'BABYUSDT',
    'babyswap': 'BABYUSDT',
    '#alch': 'ALCHUSDT', # Alchemy? Alchemix?
    '$alch': 'ALCHUSDT',
    'alch': 'ALCHUSDT',
    'alchemix': 'ALCHUSDT', # Eğer buysa
    '#sonic': 'SONICUSDT', # Alternatif zor
    '$sonic': 'SONICUSDT',
    'sonic': 'SONICUSDT',
    '#tia': 'TIAUSDT',
    '$tia': 'TIAUSDT',
    'tia': 'TIAUSDT',
    'celestia': 'TIAUSDT',
    '#id': 'IDUSDT',
    '$id': 'IDUSDT',
    'id': 'IDUSDT',
    'spaceid': 'IDUSDT',
    'space id': 'IDUSDT',
    '#mbox': 'MBOXUSDT',
    '$mbox': 'MBOXUSDT',
    'mbox': 'MBOXUSDT',
    'mobox': 'MBOXUSDT',
    '#ftn': 'FTNUSDT',
    '$ftn': 'FTNUSDT',
    'ftn': 'FTNUSDT',
    'fasttoken': 'FTNUSDT',
    '#rpl': 'RPLUSDT',
    '$rpl': 'RPLUSDT',
    'rpl': 'RPLUSDT',
    'rocketpool': 'RPLUSDT',
    'rocket pool': 'RPLUSDT',
    '#bake': 'BAKEUSDT',
    '$bake': 'BAKEUSDT',
    'bake': 'BAKEUSDT',
    'bakerytoken': 'BAKEUSDT',
    'bakery swap': 'BAKEUSDT',
    '#scr': 'SCRUSDT', # Alternatif zor
    '$scr': 'SCRUSDT',
    'scr': 'SCRUSDT',
    '#obt': 'OBTUSDT', # Alternatif zor
    '$obt': 'OBTUSDT',
    'obt': 'OBTUSDT',
    '#toshi': '1000TOSHIUSDT', # Toshi (Base)
    '$toshi': '1000TOSHIUSDT',
    'toshi': '1000TOSHIUSDT',
    '#jup': 'JUPUSDT',
    '$jup': 'JUPUSDT',
    'jup': 'JUPUSDT',
    'jupiter': 'JUPUSDT',
    '#super': 'SUPERUSDT',
    '$super': 'SUPERUSDT',
    'super': 'SUPERUSDT',
    'superverse': 'SUPERUSDT', # Eskiden SuperFarm
    'superfarm': 'SUPERUSDT',
    '#zil': 'ZILUSDT',
    '$zil': 'ZILUSDT',
    'zil': 'ZILUSDT',
    'zilliqa': 'ZILUSDT',
    '#trump': 'TRUMPUSDT', # MAGA (TRUMP)
    '$trump': 'TRUMPUSDT',
    'trump': 'TRUMPUSDT',
    'maga': 'TRUMPUSDT',
    '#f': 'FUSDT', # F Protocol? Zor.
    '$f': 'FUSDT',
    'f': 'FUSDT',
    '#uxlink': 'UXLINKUSDT', # Alternatif zor
    '$uxlink': 'UXLINKUSDT',
    'uxlink': 'UXLINKUSDT',
    '#hive': 'HIVEUSDT', # Zaten tam adı
    '$hive': 'HIVEUSDT',
    'hive': 'HIVEUSDT',
    '#dym': 'DYMUSDT',
    '$dym': 'DYMUSDT',
    'dym': 'DYMUSDT',
    'dymension': 'DYMUSDT',
    '#cake': 'CAKEUSDT',
    '$cake': 'CAKEUSDT',
    'cake': 'CAKEUSDT',
    'pancake': 'CAKEUSDT',
    'pancakeswap': 'CAKEUSDT',
    'pancake swap': 'CAKEUSDT',
    '#portal': 'PORTALUSDT', # Alternatif zor
    '$portal': 'PORTALUSDT',
    'portal': 'PORTALUSDT',
    '#xcn': 'XCNUSDT',
    '$xcn': 'XCNUSDT',
    'xcn': 'XCNUSDT',
    'onyxcoin': 'XCNUSDT', # Chain (XCN) -> Onyxcoin
    'chain': 'XCNUSDT', # Eski adı
    '#apt': 'APTUSDT',
    '$apt': 'APTUSDT',
    'apt': 'APTUSDT',
    'aptos': 'APTUSDT',
    '#tao': 'TAOUSDT',
    '$tao': 'TAOUSDT',
    'tao': 'TAOUSDT',
    'bittensor': 'TAOUSDT',
    '#aergo': 'AERGOUSDT', # Zaten tam adı
    '$aergo': 'AERGOUSDT',
    'aergo': 'AERGOUSDT',
    '#prime': 'PRIMEUSDT', # Echelon Prime
    '$prime': 'PRIMEUSDT',
    'prime': 'PRIMEUSDT',
    'echelonprime': 'PRIMEUSDT',
    'echelon prime': 'PRIMEUSDT',
    '#sca': 'SCAUSDT', # Alternatif zor
    '$sca': 'SCAUSDT',
    'sca': 'SCAUSDT',
    '#br': 'BRUSDT', # Alternatif zor
    '$br': 'BRUSDT',
    'br': 'BRUSDT',
    '#beam': 'BEAMUSDT', # Beam (Merit Circle)
    '$beam': 'BEAMUSDT',
    'beam': 'BEAMUSDT',
    'meritcirclebeam': 'BEAMUSDT',
    '#aixbt': 'AIXBTUSDT', # Alternatif zor
    '$aixbt': 'AIXBTUSDT',
    'aixbt': 'AIXBTUSDT',
    '#mdt': 'MDTUSDT',
    '$mdt': 'MDTUSDT',
    'mdt': 'MDTUSDT',
    'measurabledata': 'MDTUSDT',
    'measurable data': 'MDTUSDT',
    '#stx': 'STXUSDT',
    '$stx': 'STXUSDT',
    'stx': 'STXUSDT',
    'stacks': 'STXUSDT',
    '#perpusdt': 'PERPUSDT', # Coin adı PERP (Perpetual Protocol)
    '$perpusdt': 'PERPUSDT',
    'perpusdt': 'PERPUSDT', # Ticker'ı PERP olan coin için
    'perp': 'PERPUSDT',
    'perpetual': 'PERPUSDT',
    'perpetualprotocol': 'PERPUSDT',
    'perpetual protocol': 'PERPUSDT',
    '#fartcoin': 'FARTCOINUSDT', # Alternatif zor :)
    '$fartcoin': 'FARTCOINUSDT',
    'fartcoin': 'FARTCOINUSDT',
    '#movr': 'MOVRUSDT',
    '$movr': 'MOVRUSDT',
    'movr': 'MOVRUSDT',
    'moonriver': 'MOVRUSDT',
    '#phb': 'PHBUSDT',
    '$phb': 'PHBUSDT',
    'phb': 'PHBUSDT',
    'phoenix': 'PHBUSDT', # Phoenix Global
    'phoenixglobal': 'PHBUSDT',
    '#jst': 'JSTUSDT',
    '$jst': 'JSTUSDT',
    'jst': 'JSTUSDT',
    'just': 'JSTUSDT',
    '#ept': 'EPTUSDT', # Alternatif zor
    '$ept': 'EPTUSDT',
    'ept': 'EPTUSDT',
    '#ethbtc': 'ETHBTCUSDT', # Parite adı, alternatif yok
    '$ethbtc': 'ETHBTCUSDT',
    'ethbtc': 'ETHBTCUSDT',
    '#ethfi': 'ETHFIUSDT',
    '$ethfi': 'ETHFIUSDT',
    'ethfi': 'ETHFIUSDT',
    'etherfi': 'ETHFIUSDT',
    'ether.fi': 'ETHFIUSDT',
    '#voxel': 'VOXELUSDT',
    '$voxel': 'VOXELUSDT',
    'voxel': 'VOXELUSDT',
    'voxies': 'VOXELUSDT',
    '#avaai': 'AVAAIUSDT', # Alternatif zor
    '$avaai': 'AVAAIUSDT',
    'avaai': 'AVAAIUSDT',
    '#velodrome': 'VELODROMEUSDT', # Zaten tam adı
    '$velodrome': 'VELODROMEUSDT',
    'velodrome': 'VELODROMEUSDT',
    'velo': 'VELODROMEUSDT', # VELOUSDT ile karışabilir, dikkat
    '#bat': 'BATUSDT',
    '$bat': 'BATUSDT',
    'bat': 'BATUSDT',
    'basicattentiontoken': 'BATUSDT',
    'basic attention token': 'BATUSDT',
    '#ont': 'ONTUSDT',
    '$ont': 'ONTUSDT',
    'ont': 'ONTUSDT',
    'ontology': 'ONTUSDT',
    '#zent': 'ZENTUSDT', # Alternatif zor
    '$zent': 'ZENTUSDT',
    'zent': 'ZENTUSDT',
    '#rad': 'RADUSDT',
    '$rad': 'RADUSDT',
    'rad': 'RADUSDT',
    'radicle': 'RADUSDT',
    '#iota': 'IOTAUSDT', # Eski MIOTA, şimdi IOTA
    '$iota': 'IOTAUSDT',
    'iota': 'IOTAUSDT',
    'miota': 'IOTAUSDT', # Eski ticker
    '#cvx': 'CVXUSDT',
    '$cvx': 'CVXUSDT',
    'cvx': 'CVXUSDT',
    'convex': 'CVXUSDT',
    'convexfinance': 'CVXUSDT',
    'convex finance': 'CVXUSDT',
    '#pnut': 'PNUTUSDT', # Alternatif zor
    '$pnut': 'PNUTUSDT',
    'pnut': 'PNUTUSDT',
    '#rare': 'RAREUSDT',
    '$rare': 'RAREUSDT',
    'rare': 'RAREUSDT',
    'superrare': 'RAREUSDT',
    '#uma': 'UMAUSDT', # Zaten tam adı
    '$uma': 'UMAUSDT',
    'uma': 'UMAUSDT',
    '#one': 'ONEUSDT',
    '$one': 'ONEUSDT',
    'one': 'ONEUSDT',
    'harmony': 'ONEUSDT',
    'harmonyone': 'ONEUSDT',
    'harmony one': 'ONEUSDT',
    '#flow': 'FLOWUSDT', # Zaten tam adı
    '$flow': 'FLOWUSDT',
    'flow': 'FLOWUSDT',
    '#bsw': 'BSWUSDT',
    '$bsw': 'BSWUSDT',
    'bsw': 'BSWUSDT',
    'biswap': 'BSWUSDT',
    '#zerebro': 'ZEREBROUSDT', # Alternatif zor
    '$zerebro': 'ZEREBROUSDT',
    'zerebro': 'ZEREBROUSDT',
    '#ksm': 'KSMUSDT',
    '$ksm': 'KSMUSDT',
    'ksm': 'KSMUSDT',
    'kusama': 'KSMUSDT',
    '#ctsi': 'CTSIUSDT',
    '$ctsi': 'CTSIUSDT',
    'ctsi': 'CTSIUSDT',
    'cartesi': 'CTSIUSDT',
    '#sweat': 'SWEATUSDT',
    '$sweat': 'SWEATUSDT',
    'sweat': 'SWEATUSDT',
    'sweateconomy': 'SWEATUSDT',
    'sweat economy': 'SWEATUSDT',
    '#x': '1000XUSDT', # Strike (STRK) veya X.com (X) veya X (Twitter)? Bu çok genel.
    '$x': '1000XUSDT', # Bu 1000XUSDT için 'x' ise, spesifik bir coin adı olmalı.
    'x': '1000XUSDT',  # Şimdilik böyle kalsın, hangi X olduğu belirsiz.
    '#bel': 'BELUSDT',
    '$bel': 'BELUSDT',
    'bel': 'BELUSDT',
    'bellaprotocol': 'BELUSDT',
    'bella protocol': 'BELUSDT',
    '#myro': 'MYROUSDT', # Memecoin
    '$myro': 'MYROUSDT',
    'myro': 'MYROUSDT',
    '#vic': 'VICUSDT', # Alternatif zor
    '$vic': 'VICUSDT',
    'vic': 'VICUSDT',
    '#iotx': 'IOTXUSDT',
    '$iotx': 'IOTXUSDT',
    'iotx': 'IOTXUSDT',
    'iotex': 'IOTXUSDT',
    '#ldo': 'LDOUSDT',
    '$ldo': 'LDOUSDT',
    'ldo': 'LDOUSDT',
    'lido': 'LDOUSDT',
    'lidodao': 'LDOUSDT',
    'lido dao': 'LDOUSDT',
    '#lpt': 'LPTUSDT',
    '$lpt': 'LPTUSDT',
    'lpt': 'LPTUSDT',
    'livepeer': 'LPTUSDT',
    '#kaia': 'KAIAUSDT', # Klaytn + Finschia birleşimi
    '$kaia': 'KAIAUSDT',
    'kaia': 'KAIAUSDT',
    '#spell': 'SPELLUSDT',
    '$spell': 'SPELLUSDT',
    'spell': 'SPELLUSDT',
    'spelltoken': 'SPELLUSDT', # Abracadabra Money
    'abracadabra': 'SPELLUSDT',
    '#fwog': 'FWOGUSDT', # Alternatif zor
    '$fwog': 'FWOGUSDT',
    'fwog': 'FWOGUSDT',
    '#agi': 'AGIUSDT', # SingularityNET (AGIX oldu) -> Delysium (AGI) ?
    '$agi': 'AGIUSDT', # Eğer Delysium ise
    'agi': 'AGIUSDT',
    'delysium': 'AGIUSDT',
    '#ondo': 'ONDOUSDT', # Ondo Finance
    '$ondo': 'ONDOUSDT',
    'ondo': 'ONDOUSDT',
    'ondofinance': 'ONDOUSDT',
    '#zeta': 'ZETAUSDT',
    '$zeta': 'ZETAUSDT',
    'zeta': 'ZETAUSDT',
    'zetachain': 'ZETAUSDT',
    '#qtum': 'QTUMUSDT', # Zaten tam adı
    '$qtum': 'QTUMUSDT',
    'qtum': 'QTUMUSDT',
    '#xvs': 'XVSUSDT',
    '$xvs': 'XVSUSDT',
    'xvs': 'XVSUSDT',
    'venus': 'XVSUSDT',
    '#puffer': 'PUFFERUSDT', # Puffer Finance
    '$puffer': 'PUFFERUSDT',
    'puffer': 'PUFFERUSDT',
    'pufferfinance': 'PUFFERUSDT',
    '#lrc': 'LRCUSDT',
    '$lrc': 'LRCUSDT',
    'lrc': 'LRCUSDT',
    'loopring': 'LRCUSDT',
    '#merl': 'MERLUSDT',
    '$merl': 'MERLUSDT',
    'merl': 'MERLUSDT',
    'merlin': 'MERLUSDT',
    'merlinchain': 'MERLUSDT',
    '#fida': 'FIDAUSDT',
    '$fida': 'FIDAUSDT',
    'fida': 'FIDAUSDT',
    'bonfida': 'FIDAUSDT',
    '#mnt': 'MNTUSDT',
    '$mnt': 'MNTUSDT',
    'mnt': 'MNTUSDT',
    'mantle': 'MNTUSDT',
    '#a8': 'A8USDT', # Alternatif zor
    '$a8': 'A8USDT',
    'a8': 'A8USDT',
    '#red': 'REDUSDT', # Alternatif zor
    '$red': 'REDUSDT',
    'red': 'REDUSDT',
    '#aevo': 'AEVOUSDT', # Zaten tam adı
    '$aevo': 'AEVOUSDT',
    'aevo': 'AEVOUSDT',
    '#mln': 'MLNUSDT',
    '$mln': 'MLNUSDT',
    'mln': 'MLNUSDT',
    'melon': 'MLNUSDT', # Enzyme (MLN), eskiden Melon
    'enzyme': 'MLNUSDT',
    '#snx': 'SNXUSDT',
    '$snx': 'SNXUSDT',
    'snx': 'SNXUSDT',
    'synthetix': 'SNXUSDT',
    '#spx': 'SPXUSDT', # Alternatif zor
    '$spx': 'SPXUSDT',
    'spx': 'SPXUSDT',
    '#sign': 'SIGNUSDT', # Alternatif zor
    '$sign': 'SIGNUSDT',
    'sign': 'SIGNUSDT',
    '#dydx': 'DYDXUSDT', # Zaten tam adı
    '$dydx': 'DYDXUSDT',
    'dydx': 'DYDXUSDT',
    '#steem': 'STEEMUSDT', # Zaten tam adı
    '$steem': 'STEEMUSDT',
    'steem': 'STEEMUSDT',
    '#kas': 'KASUSDT',
    '$kas': 'KASUSDT',
    'kas': 'KASUSDT',
    'kaspa': 'KASUSDT',
    '#xai': 'XAIUSDT', # Xai Games
    '$xai': 'XAIUSDT',
    'xai': 'XAIUSDT',
    'xaigames': 'XAIUSDT',
    '#omni': 'OMNIUSDT',
    '$omni': 'OMNIUSDT',
    'omni': 'OMNIUSDT',
    'omninetwork': 'OMNIUSDT',
    '#qnt': 'QNTUSDT',
    '$qnt': 'QNTUSDT',
    'qnt': 'QNTUSDT',
    'quant': 'QNTUSDT',
    '#xvg': 'XVGUSDT',
    '$xvg': 'XVGUSDT',
    'xvg': 'XVGUSDT',
    'verge': 'XVGUSDT',
    '#flux': 'FLUXUSDT', # Zaten tam adı
    '$flux': 'FLUXUSDT',
    'flux': 'FLUXUSDT',
    '#stpt': 'STPTUSDT',
    '$stpt': 'STPTUSDT',
    'stpt': 'STPTUSDT',
    'stp': 'STPTUSDT', # Standard Tokenization Protocol
    '#ronin': 'RONINUSDT', # Zaten tam adı
    '$ronin': 'RONINUSDT',
    'ronin': 'RONINUSDT',
    'ron': 'RONINUSDT', # Sıkça kullanılır
    '#akt': 'AKTUSDT',
    '$akt': 'AKTUSDT',
    'akt': 'AKTUSDT',
    'akash': 'AKTUSDT',
    'akashnetwork': 'AKTUSDT',
    'akash network': 'AKTUSDT',
    '#cats': '1000CATSUSDT', # CATS (BRC-20)
    '$cats': '1000CATSUSDT',
    'cats': '1000CATSUSDT',
    '#nmr': 'NMRUSDT',
    '$nmr': 'NMRUSDT',
    'nmr': 'NMRUSDT',
    'numeraire': 'NMRUSDT',
    '#vet': 'VETUSDT',
    '$vet': 'VETUSDT',
    'vet': 'VETUSDT',
    'vechain': 'VETUSDT',
    '#meme': 'MEMEUSDT', # Memecoin (MEME)
    '$meme': 'MEMEUSDT',
    'meme': 'MEMEUSDT',
    'memecoin': 'MEMEUSDT',
    '#nfp': 'NFPUSDT',
    '$nfp': 'NFPUSDT',
    'nfp': 'NFPUSDT',
    'nfprompt': 'NFPUSDT',
    '#osmo': 'OSMOUSDT',
    '$osmo': 'OSMOUSDT',
    'osmo': 'OSMOUSDT',
    'osmosis': 'OSMOUSDT',
    '#1inch': '1INCHUSDT', # Zaten tam adı
    '$1inch': '1INCHUSDT',
    '1inch': '1INCHUSDT',
    'oneinch': '1INCHUSDT',
    '#aioz': 'AIOZUSDT',
    '$aioz': 'AIOZUSDT',
    'aioz': 'AIOZUSDT',
    'aioznetwork': 'AIOZUSDT',
    'aioz network': 'AIOZUSDT',
    '#obol': 'OBOLUSDT', # Alternatif zor
    '$obol': 'OBOLUSDT',
    'obol': 'OBOLUSDT',
    '#sushi': 'SUSHIUSDT',
    '$sushi': 'SUSHIUSDT',
    'sushi': 'SUSHIUSDT',
    'sushiswap': 'SUSHIUSDT',
    'sushi swap': 'SUSHIUSDT',
    '#duck': 'DUCKUSDT', # Alternatif zor
    '$duck': 'DUCKUSDT',
    'duck': 'DUCKUSDT',
    '#virtual': 'VIRTUALUSDT', # Alternatif zor
    '$virtual': 'VIRTUALUSDT',
    'virtual': 'VIRTUALUSDT',
    '#polyx': 'POLYXUSDT',
    '$polyx': 'POLYXUSDT',
    'polyx': 'POLYXUSDT',
    'polymesh': 'POLYXUSDT',
    '#kda': 'KDAUSDT',
    '$kda': 'KDAUSDT',
    'kda': 'KDAUSDT',
    'kadena': 'KDAUSDT',
    '#theta': 'THETAUSDT', # Theta Network
    '$theta': 'THETAUSDT',
    'theta': 'THETAUSDT',
    'thetanetwork': 'THETAUSDT',
    'theta network': 'THETAUSDT',
    '#woo': 'WOOUSDT',
    '$woo': 'WOOUSDT',
    'woo': 'WOOUSDT',
    'woonetwork': 'WOOUSDT',
    'woo network': 'WOOUSDT',
    '#bera': 'BERAUSDT',
    '$bera': 'BERAUSDT',
    'bera': 'BERAUSDT',
    'berachain': 'BERAUSDT',
    '#milk': 'MILKUSDT', # Alternatif zor
    '$milk': 'MILKUSDT',
    'milk': 'MILKUSDT',
    '#enj': 'ENJUSDT',
    '$enj': 'ENJUSDT',
    'enj': 'ENJUSDT',
    'enjin': 'ENJUSDT',
    'enjincoin': 'ENJUSDT',
    'enjin coin': 'ENJUSDT',
    '#api3': 'API3USDT', # Zaten tam adı
    '$api3': 'API3USDT',
    'api3': 'API3USDT',
    '#waxp': 'WAXPUSDT',
    '$waxp': 'WAXPUSDT',
    'waxp': 'WAXPUSDT',
    'wax': 'WAXPUSDT',
    '#wif': 'WIFUSDT', # dogwifhat
    '$wif': 'WIFUSDT',
    'wif': 'WIFUSDT',
    'dogwifhat': 'WIFUSDT',
    'dog wif hat': 'WIFUSDT',
    '#ens': 'ENSUSDT',
    '$ens': 'ENSUSDT',
    'ens': 'ENSUSDT',
    'ethereumnameservice': 'ENSUSDT',
    'ethereum name service': 'ENSUSDT',
    '#lista': 'LISTAUSDT', # Lista DAO
    '$lista': 'LISTAUSDT',
    'lista': 'LISTAUSDT',
    'listadao': 'LISTAUSDT',
    '#gps': 'GPSUSDT', # Alternatif zor
    '$gps': 'GPSUSDT',
    'gps': 'GPSUSDT',
    '#vine': 'VINEUSDT', # Alternatif zor
    '$vine': 'VINEUSDT',
    'vine': 'VINEUSDT',
    '#slerf': 'SLERFUSDT', # Memecoin
    '$slerf': 'SLERFUSDT',
    'slerf': 'SLERFUSDT',
    '#dexe': 'DEXEUSDT',
    '$dexe': 'DEXEUSDT',
    'dexe': 'DEXEUSDT',
    'deriexchange': 'DEXEUSDT', # DeXe (Decentralized Social Trading Platform)
    '#rss3': 'RSS3USDT', # Zaten tam adı
    '$rss3': 'RSS3USDT',
    'rss3': 'RSS3USDT',
    '#auction': 'AUCTIONUSDT', # Bounce Finance (AUCTION)
    '$auction': 'AUCTIONUSDT',
    'auction': 'AUCTIONUSDT',
    'bounce': 'AUCTIONUSDT',
    'bouncefinance': 'AUCTIONUSDT',
    '#edu': 'EDUUSDT',
    '$edu': 'EDUUSDT',
    'edu': 'EDUUSDT',
    'openedu': 'EDUUSDT', # Open Campus
    'opencampus': 'EDUUSDT',
    '#why': '10000WHYUSDT', # Alternatif zor
    '$why': '10000WHYUSDT',
    'why': '10000WHYUSDT',
    '#arkm': 'ARKMUSDT',
    '$arkm': 'ARKMUSDT',
    'arkm': 'ARKMUSDT',
    'arkham': 'ARKMUSDT',
    '#lever': 'LEVERUSDT', # LeverFi
    '$lever': 'LEVERUSDT',
    'lever': 'LEVERUSDT',
    'leverfi': 'LEVERUSDT',
    '#glmr': 'GLMRUSDT',
    '$glmr': 'GLMRUSDT',
    'glmr': 'GLMRUSDT',
    'moonbeam': 'GLMRUSDT',
    '#xion': 'XIONUSDT', # Alternatif zor
    '$xion': 'XIONUSDT',
    'xion': 'XIONUSDT',
    '#hnt': 'HNTUSDT',
    '$hnt': 'HNTUSDT',
    'hnt': 'HNTUSDT',
    'helium': 'HNTUSDT',
    '#alice': 'ALICEUSDT',
    '$alice': 'ALICEUSDT',
    'alice': 'ALICEUSDT',
    'myneighboralice': 'ALICEUSDT',
    'my neighbor alice': 'ALICEUSDT',
    '#slf': 'SLFUSDT', # Alternatif zor
    '$slf': 'SLFUSDT',
    'slf': 'SLFUSDT',
    '#data': 'DATAUSDT', # Streamr (DATA)
    '$data': 'DATAUSDT',
    'data': 'DATAUSDT',
    'streamr': 'DATAUSDT',
    '#wal': 'WALUSDT', # Alternatif zor
    '$wal': 'WALUSDT',
    'wal': 'WALUSDT',
    '#neirocto': '1000NEIROCTOUSDT', # Alternatif zor
    '$neirocto': '1000NEIROCTOUSDT',
    'neirocto': '1000NEIROCTOUSDT',
    '#cfx': 'CFXUSDT',
    '$cfx': 'CFXUSDT',
    'cfx': 'CFXUSDT',
    'conflux': 'CFXUSDT',
    '#paxg': 'PAXGUSDT', # Pax Gold
    '$paxg': 'PAXGUSDT',
    'paxg': 'PAXGUSDT',
    'paxgold': 'PAXGUSDT',
    'pax gold': 'PAXGUSDT',
    '#mina': 'MINAUSDT', # Mina Protocol
    '$mina': 'MINAUSDT',
    'mina': 'MINAUSDT',
    'minaprotocol': 'MINAUSDT',
    '#cos': 'COSUSDT',
    '$cos': 'COSUSDT',
    'cos': 'COSUSDT',
    'contentos': 'COSUSDT',
    '#ponke': 'PONKEUSDT', # Memecoin
    '$ponke': 'PONKEUSDT',
    'ponke': 'PONKEUSDT',
    '#pengu': 'PENGUUSDT', # Alternatif zor
    '$pengu': 'PENGUUSDT',
    'pengu': 'PENGUUSDT',
    '#io': 'IOUSDT', # io.net
    '$io': 'IOUSDT',
    'io': 'IOUSDT',
    'ionet': 'IOUSDT',
    'io.net': 'IOUSDT',
    '#token': 'TOKENUSDT', # TokenFi
    '$token': 'TOKENUSDT',
    'token': 'TOKENUSDT',
    'tokenfi': 'TOKENUSDT',
    '#hft': 'HFTUSDT',
    '$hft': 'HFTUSDT',
    'hft': 'HFTUSDT',
    'hashflow': 'HFTUSDT',
    '#pol': 'POLUSDT', # Polygon Ecosystem Token
    '$pol': 'POLUSDT',
    'pol': 'POLUSDT',
    'polygonecosystem': 'POLUSDT',
    '#zora': 'ZORAUSDT', # Alternatif zor
    '$zora': 'ZORAUSDT',
    'zora': 'ZORAUSDT',
    '#ace': 'ACEUSDT', # Fusionist (ACE)
    '$ace': 'ACEUSDT',
    'ace': 'ACEUSDT',
    'fusionist': 'ACEUSDT',
    '#mumu': '1000MUMUUSDT', # Memecoin
    '$mumu': '1000MUMUUSDT',
    'mumu': '1000MUMUUSDT',
    '#tai': 'TAIUSDT', # Alternatif zor
    '$tai': 'TAIUSDT',
    'tai': 'TAIUSDT',
    '#prcl': 'PRCLUSDT',
    '$prcl': 'PRCLUSDT',
    'prcl': 'PRCLUSDT',
    'parcl': 'PRCLUSDT',
    '#not': 'NOTUSDT', # Notcoin
    '$not': 'NOTUSDT',
    'not': 'NOTUSDT',
    'notcoin': 'NOTUSDT',
    '#ns': 'NSUSDT', # Alternatif zor
    '$ns': 'NSUSDT',
    'ns': 'NSUSDT',
    '#mask': 'MASKUSDT', # Mask Network
    '$mask': 'MASKUSDT',
    'mask': 'MASKUSDT',
    'masknetwork': 'MASKUSDT',
    '#solayer': 'SOLAYERUSDT', # Alternatif zor
    '$solayer': 'SOLAYERUSDT',
    'solayer': 'SOLAYERUSDT',
    '#bal': 'BALUSDT',
    '$bal': 'BALUSDT',
    'bal': 'BALUSDT',
    'balancer': 'BALUSDT',
    '#twt': 'TWTUSDT',
    '$twt': 'TWTUSDT',
    'twt': 'TWTUSDT',
    'trustwallet': 'TWTUSDT',
    'trust wallet token': 'TWTUSDT',
    '#cheems': '1000000CHEEMSUSDT', # Memecoin
    '$cheems': '1000000CHEEMSUSDT',
    'cheems': '1000000CHEEMSUSDT',
    '#wld': 'WLDUSDT',
    '$wld': 'WLDUSDT',
    'wld': 'WLDUSDT',
    'worldcoin': 'WLDUSDT',
    'world coin': 'WLDUSDT',
    '#mvl': 'MVLUSDT', # MVL (Mass Vehicle Ledger)
    '$mvl': 'MVLUSDT',
    'mvl': 'MVLUSDT',
    'massvehicleledger': 'MVLUSDT',
    '#gods': 'GODSUSDT', # Gods Unchained
    '$gods': 'GODSUSDT',
    'gods': 'GODSUSDT',
    'godsunchained': 'GODSUSDT',
    '#acx': 'ACXUSDT', # Alternatif zor
    '$acx': 'ACXUSDT',
    'acx': 'ACXUSDT',
    '#bigtime': 'BIGTIMEUSDT', # Zaten tam adı
    '$bigtime': 'BIGTIMEUSDT',
    'bigtime': 'BIGTIMEUSDT',
    '#om': 'OMUSDT', # MANTRA (OM)
    '$om': 'OMUSDT',
    'om': 'OMUSDT',
    'mantra': 'OMUSDT',
    'mantradao': 'OMUSDT', # Eski adı
    '#mog': '1000000MOGUSDT', # Memecoin
    '$mog': '1000000MOGUSDT',
    'mog': '1000000MOGUSDT',
    'mogcoin': '1000000MOGUSDT',
    '#dodo': 'DODOUSDT', # Zaten tam adı
    '$dodo': 'DODOUSDT',
    'dodo': 'DODOUSDT',
    '#hifi': 'HIFIUSDT', # Hifi Finance (eskiden Mainframe)
    '$hifi': 'HIFIUSDT',
    'hifi': 'HIFIUSDT',
    'hififinance': 'HIFIUSDT',
    'mainframe': 'HIFIUSDT', # Eski adı
    '#zec': 'ZECUSDT',
    '$zec': 'ZECUSDT',
    'zec': 'ZECUSDT',
    'zcash': 'ZECUSDT',
    '#astr': 'ASTRUSDT',
    '$astr': 'ASTRUSDT',
    'astr': 'ASTRUSDT',
    'astar': 'ASTRUSDT',
    '#apu': '1000APUUSDT', # Memecoin (Apu Apustaja)
    '$apu': '1000APUUSDT',
    'apu': '1000APUUSDT',
    'apuapustaja': '1000APUUSDT',
    '#sys': 'SYSUSDT',
    '$sys': 'SYSUSDT',
    'sys': 'SYSUSDT',
    'syscoin': 'SYSUSDT',
    '#major': 'MAJORUSDT', # Alternatif zor
    '$major': 'MAJORUSDT',
    'major': 'MAJORUSDT',
    '#tru': 'TRUUSDT', # TrueFi
    '$tru': 'TRUUSDT',
    'tru': 'TRUUSDT',
    'truefi': 'TRUUSDT',
    '#prom': 'PROMUSDT', # Prom
    '$prom': 'PROMUSDT',
    'prom': 'PROMUSDT',
    '#ai16z': 'AI16ZUSDT', # Alternatif zor
    '$ai16z': 'AI16ZUSDT',
    'ai16z': 'AI16ZUSDT',
    '#hei': 'HEIUSDT', # Alternatif zor
    '$hei': 'HEIUSDT',
    'hei': 'HEIUSDT',
    '#audio': 'AUDIOUSDT', # Audius
    '$audio': 'AUDIOUSDT',
    'audio': 'AUDIOUSDT',
    'audius': 'AUDIOUSDT',
    '#badger': 'BADGERUSDT', # Badger DAO
    '$badger': 'BADGERUSDT',
    'badger': 'BADGERUSDT',
    'badgerdao': 'BADGERUSDT',
    '#sc': 'SCUSDT', # Siacoin
    '$sc': 'SCUSDT',
    'sc': 'SCUSDT',
    'siacoin': 'SCUSDT',
    '#rex': 'REXUSDT', # Alternatif zor
    '$rex': 'REXUSDT',
    'rex': 'REXUSDT',
    '#rez': 'REZUSDT', # Renzo
    '$rez': 'REZUSDT',
    'rez': 'REZUSDT',
    'renzo': 'REZUSDT',
    '#swell': 'SWELLUSDT', # Swell Network
    '$swell': 'SWELLUSDT',
    'swell': 'SWELLUSDT',
    'swellnetwork': 'SWELLUSDT',
    '#mobile': 'MOBILEUSDT', # Helium Mobile
    '$mobile': 'MOBILEUSDT',
    'mobile': 'MOBILEUSDT',
    'heliummobile': 'MOBILEUSDT',
    '#tlm': 'TLMUSDT', # Alien Worlds
    '$tlm': 'TLMUSDT',
    'tlm': 'TLMUSDT',
    'alienworlds': 'TLMUSDT',
    'alien worlds': 'TLMUSDT',
    '#sei': 'SEIUSDT', # Sei Network
    '$sei': 'SEIUSDT',
    'sei': 'SEIUSDT',
    'seinetwork': 'SEIUSDT',
    '#luna2': 'LUNA2USDT', # Terra 2.0
    '$luna2': 'LUNA2USDT',
    'luna2': 'LUNA2USDT',
    'terra2': 'LUNA2USDT',
    'terraluna2': 'LUNA2USDT',
    '#bmt': 'BMTUSDT', # Alternatif zor
    '$bmt': 'BMTUSDT',
    'bmt': 'BMTUSDT',
    '#dent': 'DENTUSDT', # Zaten tam adı
    '$dent': 'DENTUSDT',
    'dent': 'DENTUSDT',
    '#alu': 'ALUUSDT', # Altura
    '$alu': 'ALUUSDT',
    'alu': 'ALUUSDT',
    'altura': 'ALUUSDT',
    '#xem': 'XEMUSDT', # NEM
    '$xem': 'XEMUSDT',
    'xem': 'XEMUSDT',
    'nem': 'XEMUSDT',
    '#agld': 'AGLDUSDT', # Adventure Gold
    '$agld': 'AGLDUSDT',
    'agld': 'AGLDUSDT',
    'adventuregold': 'AGLDUSDT',
    '#cvc': 'CVCUSDT', # Civic
    '$cvc': 'CVCUSDT',
    'cvc': 'CVCUSDT',
    'civic': 'CVCUSDT',
    '#popcat': 'POPCATUSDT', # Memecoin
    '$popcat': 'POPCATUSDT',
    'popcat': 'POPCATUSDT',
    '#vanry': 'VANRYUSDT', # Vanar Chain (eskiden Terra Virtua Kolect)
    '$vanry': 'VANRYUSDT',
    'vanry': 'VANRYUSDT',
    'vanarchain': 'VANRYUSDT',
    'tvk': 'VANRYUSDT', # Eski ticker
    'terravirtua': 'VANRYUSDT',
    '#bb': 'BBUSDT', # BounceBit
    '$bb': 'BBUSDT',
    'bb': 'BBUSDT',
    'bouncebit': 'BBUSDT',
    '#jto': 'JTOUSDT', # Jito
    '$jto': 'JTOUSDT',
    'jto': 'JTOUSDT',
    'jito': 'JTOUSDT',
    '#ethw': 'ETHWUSDT', # EthereumPoW
    '$ethw': 'ETHWUSDT',
    'ethw': 'ETHWUSDT',
    'ethereumpow': 'ETHWUSDT',
    '#kernel': 'KERNELUSDT', # Alternatif zor
    '$kernel': 'KERNELUSDT',
    'kernel': 'KERNELUSDT',
    '#lumia': 'LUMIAUSDT', # Alternatif zor
    '$lumia': 'LUMIAUSDT',
    'lumia': 'LUMIAUSDT',
    '#looks': 'LOOKSUSDT', # LooksRare
    '$looks': 'LOOKSUSDT',
    'looks': 'LOOKSUSDT',
    'looksrare': 'LOOKSUSDT',
    '#rose': 'ROSEUSDT', # Oasis Network
    '$rose': 'ROSEUSDT',
    'rose': 'ROSEUSDT',
    'oasis': 'ROSEUSDT',
    'oasisnetwork': 'ROSEUSDT',
    '#mew': 'MEWUSDT', # Cat in a dogs world (MEW)
    '$mew': 'MEWUSDT',
    'mew': 'MEWUSDT',
    'catdogsworld': 'MEWUSDT',
    '#aero': 'AEROUSDT', # Aerodrome Finance
    '$aero': 'AEROUSDT',
    'aero': 'AEROUSDT',
    'aerodrome': 'AEROUSDT',
    'aerodromefinance': 'AEROUSDT',
    '#core': 'COREUSDT', # Core DAO
    '$core': 'COREUSDT',
    'core': 'COREUSDT',
    'coredao': 'COREUSDT',
    '#rsr': 'RSRUSDT', # Reserve Rights
    '$rsr': 'RSRUSDT',
    'rsr': 'RSRUSDT',
    'reserverights': 'RSRUSDT',
    '#avl': 'AVLUSDT', # Alternatif zor
    '$avl': 'AVLUSDT',
    'avl': 'AVLUSDT',
    '#peipei': '1000000PEIPEIUSDT', # Memecoin
    '$peipei': '1000000PEIPEIUSDT',
    'peipei': '1000000PEIPEIUSDT',
    '#gun': 'GUNUSDT', # Alternatif zor
    '$gun': 'GUNUSDT',
    'gun': 'GUNUSDT',
    '#fuel': 'FUELUSDT', # Alternatif zor (Jetfuel Finance?)
    '$fuel': 'FUELUSDT',
    'fuel': 'FUELUSDT',
    '#vvv': 'VVVUSDT', # Alternatif zor
    '$vvv': 'VVVUSDT',
    'vvv': 'VVVUSDT',
    '#celo': 'CELOUSDT', # Zaten tam adı
    '$celo': 'CELOUSDT',
    'celo': 'CELOUSDT',
    '#hmstr': 'HMSTRUSDT', # Alternatif zor
    '$hmstr': 'HMSTRUSDT',
    'hmstr': 'HMSTRUSDT',
    '#degen': 'DEGENUSDT', # Degen (Base)
    '$degen': 'DEGENUSDT',
    'degen': 'DEGENUSDT',
    '#render': 'RENDERUSDT', # Render Token
    '$render': 'RENDERUSDT',
    'render': 'RENDERUSDT',
    'rndr': 'RENDERUSDT', # Sıkça kullanılır
    'rendertoken': 'RENDERUSDT',
    '#plume': 'PLUMEUSDT', # Alternatif zor
    '$plume': 'PLUMEUSDT',
    'plume': 'PLUMEUSDT',
    '#chillguy': 'CHILLGUYUSDT', # Alternatif zor
    '$chillguy': 'CHILLGUYUSDT',
    'chillguy': 'CHILLGUYUSDT',
    '#send': 'SENDUSDT', # Alternatif zor
    '$send': 'SENDUSDT',
    'send': 'SENDUSDT',
    '#tnsr': 'TNSRUSDT', # Tensor
    '$tnsr': 'TNSRUSDT',
    'tnsr': 'TNSRUSDT',
    'tensor': 'TNSRUSDT',
    '#vtho': 'VTHOUSDT', # VeThor Token
    '$vtho': 'VTHOUSDT',
    'vtho': 'VTHOUSDT',
    'vethor': 'VTHOUSDT',
    'vethortoken': 'VTHOUSDT',
    '#coti': 'COTIUSDT', # Zaten tam adı
    '$coti': 'COTIUSDT',
    'coti': 'COTIUSDT',
    '#blur': 'BLURUSDT', # Zaten tam adı
    '$blur': 'BLURUSDT',
    'blur': 'BLURUSDT',
    '#kava': 'KAVAUSDT', # Zaten tam adı
    '$kava': 'KAVAUSDT',
    'kava': 'KAVAUSDT',
    '#taiko': 'TAIKOUSDT', # Zaten tam adı
    '$taiko': 'TAIKOUSDT',
    'taiko': 'TAIKOUSDT',
    '#drift': 'DRIFTUSDT', # Drift Protocol
    '$drift': 'DRIFTUSDT',
    'drift': 'DRIFTUSDT',
    'driftprotocol': 'DRIFTUSDT',
    '#move': 'MOVEUSDT', # Alternatif zor
    '$move': 'MOVEUSDT',
    'move': 'MOVEUSDT',
    '#griffain': 'GRIFFAINUSDT', # Alternatif zor
    '$griffain': 'GRIFFAINUSDT',
    'griffain': 'GRIFFAINUSDT',
    '#bsv': 'BSVUSDT', # Bitcoin SV
    '$bsv': 'BSVUSDT',
    'bsv': 'BSVUSDT',
    'bitcoinsv': 'BSVUSDT',
    'bitcoin sv': 'BSVUSDT',
    '#bome': 'BOMEUSDT', # Book of Meme
    '$bome': 'BOMEUSDT',
    'bome': 'BOMEUSDT',
    'bookofmeme': 'BOMEUSDT',
    '#qubic': '10000QUBICUSDT', # Qubic
    '$qubic': '10000QUBICUSDT',
    'qubic': '10000QUBICUSDT',
    '#tut': 'TUTUSDT', # Alternatif zor
    '$tut': 'TUTUSDT',
    'tut': 'TUTUSDT',
    '#ena': 'ENAUSDT', # Ethena
    '$ena': 'ENAUSDT',
    'ena': 'ENAUSDT',
    'ethena': 'ENAUSDT',
    '#dgb': 'DGBUSDT', # DigiByte
    '$dgb': 'DGBUSDT',
    'dgb': 'DGBUSDT',
    'digibyte': 'DGBUSDT',
    '#kmno': 'KMNOUSDT', # Kamino
    '$kmno': 'KMNOUSDT',
    'kmno': 'KMNOUSDT',
    'kamino': 'KMNOUSDT',
    '#chr': 'CHRUSDT', # Chromia
    '$chr': 'CHRUSDT',
    'chr': 'CHRUSDT',
    'chromia': 'CHRUSDT',
    '#l3': 'L3USDT', # Alternatif zor
    '$l3': 'L3USDT',
    'l3': 'L3USDT',
    '#flm': 'FLMUSDT', # Flamingo Finance
    '$flm': 'FLMUSDT',
    'flm': 'FLMUSDT',
    'flamingo': 'FLMUSDT',
    'flamingofinance': 'FLMUSDT',
    '#joe': 'JOEUSDT', # Trader Joe
    '$joe': 'JOEUSDT',
    'joe': 'JOEUSDT',
    'traderjoe': 'JOEUSDT',
    '#flock': 'FLOCKUSDT', # Alternatif zor
    '$flock': 'FLOCKUSDT',
    'flock': 'FLOCKUSDT',
    '#parti': 'PARTIUSDT', # Alternatif zor
    '$parti': 'PARTIUSDT',
    'parti': 'PARTIUSDT',
    '#arb': 'ARBUSDT', # Arbitrum
    '$arb': 'ARBUSDT',
    'arb': 'ARBUSDT',
    'arbitrum': 'ARBUSDT',
    '#jellyjelly': 'JELLYJELLYUSDT', # Alternatif zor
    '$jellyjelly': 'JELLYJELLYUSDT',
    'jellyjelly': 'JELLYJELLYUSDT',
    '#cgpt': 'CGPTUSDT', # ChainGPT
    '$cgpt': 'CGPTUSDT',
    'cgpt': 'CGPTUSDT',
    'chaingpt': 'CGPTUSDT',
    '#fb': 'FBUSDT', # Alternatif zor (Fenerbahçe Fan Token?)
    '$fb': 'FBUSDT',
    'fb': 'FBUSDT',
    'fenerbahce': 'FBUSDT', # Eğer buysa
    '#wct': 'WCTUSDT', # Alternatif zor
    '$wct': 'WCTUSDT',
    'wct': 'WCTUSDT',
    '#pendle': 'PENDLEUSDT', # Zaten tam adı
    '$pendle': 'PENDLEUSDT',
    'pendle': 'PENDLEUSDT',
    '#ankr': 'ANKRUSDT', # Zaten tam adı
    '$ankr': 'ANKRUSDT',
    'ankr': 'ANKRUSDT',
    '#hyper': 'HYPERUSDT', # Alternatif zor
    '$hyper': 'HYPERUSDT',
    'hyper': 'HYPERUSDT',
    '#saga': 'SAGAUSDT', # Zaten tam adı
    '$saga': 'SAGAUSDT',
    'saga': 'SAGAUSDT',
    '#sxp': 'SXPUSDT', # Swipe (artık Solar - SXP)
    '$sxp': 'SXPUSDT',
    'sxp': 'SXPUSDT',
    'swipe': 'SXPUSDT', # Eski adı
    'solar': 'SXPUSDT', # Yeni adı
    '#c98': 'C98USDT', # Coin98
    '$c98': 'C98USDT',
    'c98': 'C98USDT',
    'coin98': 'C98USDT',
    '#gas': 'GASUSDT', # Neo Gas
    '$gas': 'GASUSDT',
    'gas': 'GASUSDT',
    'neogas': 'GASUSDT',
    '#banana': 'BANANAUSDT', # Banana Gun
    '$banana': 'BANANAUSDT',
    'banana': 'BANANAUSDT',
    'bananagun': 'BANANAUSDT',
    '#kaito': 'KAITOUSDT', # Alternatif zor
    '$kaito': 'KAITOUSDT',
    'kaito': 'KAITOUSDT',
    '#high': 'HIGHUSDT', # Highstreet
    '$high': 'HIGHUSDT',
    'high': 'HIGHUSDT',
    'highstreet': 'HIGHUSDT',
    '#velo': 'VELOUSDT', # Velodrome Finance (VELO ticker'ı) - Dikkat VELODROMEUSDT ile karışmasın
    '$velo': 'VELOUSDT',
    'velo': 'VELOUSDT', # Bu VELO, diğeri VELODROME
    '#chess': 'CHESSUSDT', # Tranchess
    '$chess': 'CHESSUSDT',
    'chess': 'CHESSUSDT',
    'tranchess': 'CHESSUSDT',
    '#michi': 'MICHIUSDT', # Memecoin
    '$michi': 'MICHIUSDT',
    'michi': 'MICHIUSDT',
    '#carv': 'CARVUSDT', # Zaten tam adı
    '$carv': 'CARVUSDT',
    'carv': 'CARVUSDT',
    '#memefi': 'MEMEFIUSDT', # Zaten tam adı
    '$memefi': 'MEMEFIUSDT',
    'memefi': 'MEMEFIUSDT',
    '#ark': 'ARKUSDT', # Zaten tam adı
    '$ark': 'ARKUSDT',
    'ark': 'ARKUSDT',
    '#bananas31': 'BANANAS31USDT', # Alternatif zor
    '$bananas31': 'BANANAS31USDT',
    'bananas31': 'BANANAS31USDT',
    '#lqty': 'LQTYUSDT', # Liquity
    '$lqty': 'LQTYUSDT',
    'lqty': 'LQTYUSDT',
    'liquity': 'LQTYUSDT',
    '#chz': 'CHZUSDT', # Chiliz
    '$chz': 'CHZUSDT',
    'chz': 'CHZUSDT',
    'chiliz': 'CHZUSDT',
    '#ntrn': 'NTRNUSDT', # Neutron
    '$ntrn': 'NTRNUSDT',
    'ntrn': 'NTRNUSDT',
    'neutron': 'NTRNUSDT',
    '#order': 'ORDERUSDT', # Alternatif zor
    '$order': 'ORDERUSDT',
    'order': 'ORDERUSDT',
    '#zeus': 'ZEUSUSDT', # Zeus Network
    '$zeus': 'ZEUSUSDT',
    'zeus': 'ZEUSUSDT',
    'zeusnetwork': 'ZEUSUSDT',
    '#zbcn': 'ZBCNUSDT', # Zebec Network (ZBCN) - Zebec Protocol (ZBC) ile karışabilir
    '$zbcn': 'ZBCNUSDT',
    'zbcn': 'ZBCNUSDT',
    'zebecnetwork': 'ZBCNUSDT',
    '#vana': 'VANAUSDT', # Alternatif zor
    '$vana': 'VANAUSDT',
    'vana': 'VANAUSDT',
    '#anime': 'ANIMEUSDT', # Alternatif zor
    '$anime': 'ANIMEUSDT',
    'anime': 'ANIMEUSDT',
    '#knc': 'KNCUSDT', # Kyber Network Crystal
    '$knc': 'KNCUSDT',
    'knc': 'KNCUSDT',
    'kyber': 'KNCUSDT',
    'kybernetwork': 'KNCUSDT',
    '#mtl': 'MTLUSDT', # Metal DAO (eskiden MetalPay)
    '$mtl': 'MTLUSDT',
    'mtl': 'MTLUSDT',
    'metal': 'MTLUSDT',
    'metaldao': 'MTLUSDT',
    '#brett': 'BRETTUSDT', # Memecoin (Base)
    '$brett': 'BRETTUSDT',
    'brett': 'BRETTUSDT',
    '#dogs': 'DOGSUSDT', # Memecoin (Runes?)
    '$dogs': 'DOGSUSDT',
    'dogs': 'DOGSUSDT',
    '#gomining': 'GOMININGUSDT', # GoMining Token
    '$gomining': 'GOMININGUSDT',
    'gomining': 'GOMININGUSDT',
    '#xno': 'XNOUSDT', # Nano
    '$xno': 'XNOUSDT',
    'xno': 'XNOUSDT',
    'nano': 'XNOUSDT',
    '#siren': 'SIRENUSDT', # Alternatif zor
    '$siren': 'SIRENUSDT',
    'siren': 'SIRENUSDT',
    '#boba': 'BOBAUSDT', # Boba Network
    '$boba': 'BOBAUSDT',
    'boba': 'BOBAUSDT',
    'bobanetwork': 'BOBAUSDT',
    '#deep': 'DEEPUSDT', # Alternatif zor
    '$deep': 'DEEPUSDT',
    'deep': 'DEEPUSDT',
    '#safe': 'SAFEUSDT', # Gnosis Safe (yeni Safe Token)
    '$safe': 'SAFEUSDT',
    'safe': 'SAFEUSDT',
    'safetoken': 'SAFEUSDT',
    '#rvn': 'RVNUSDT', # Ravencoin
    '$rvn': 'RVNUSDT',
    'rvn': 'RVNUSDT',
    'ravencoin': 'RVNUSDT',
    '#hippo': 'HIPPOUSDT', # Alternatif zor
    '$hippo': 'HIPPOUSDT',
    'hippo': 'HIPPOUSDT',
    '#me': 'MEUSDT', # Alternatif zor
    '$me': 'MEUSDT',
    'me': 'MEUSDT',
    '#xdc': 'XDCUSDT', # XDC Network (XinFin)
    '$xdc': 'XDCUSDT',
    'xdc': 'XDCUSDT',
    'xdcnetwork': 'XDCUSDT',
    'xinfin': 'XDCUSDT',
    '#crv': 'CRVUSDT', # Curve DAO Token
    '$crv': 'CRVUSDT',
    'crv': 'CRVUSDT',
    'curve': 'CRVUSDT',
    'curvedao': 'CRVUSDT',
    '#masa': 'MASAUSDT', # Masa Network
    '$masa': 'MASAUSDT',
    'masa': 'MASAUSDT',
    'masanetwork': 'MASAUSDT',
    '#broccoli': 'BROCCOLIUSDT', # Alternatif zor
    '$broccoli': 'BROCCOLIUSDT',
    'broccoli': 'BROCCOLIUSDT',
    '#quick': 'QUICKUSDT', # QuickSwap
    '$quick': 'QUICKUSDT',
    'quick': 'QUICKUSDT',
    'quickswap': 'QUICKUSDT',
    '#solo': 'SOLOUSDT', # Sologenic
    '$solo': 'SOLOUSDT',
    'solo': 'SOLOUSDT',
    'sologenic': 'SOLOUSDT',
    '#alt': 'ALTUSDT', # AltLayer
    '$alt': 'ALTUSDT',
    'alt': 'ALTUSDT',
    'altlayer': 'ALTUSDT',
    '#seraph': 'SERAPHUSDT', # Alternatif zor
    '$seraph': 'SERAPHUSDT',
    'seraph': 'SERAPHUSDT',
    '#inj': 'INJUSDT', # Injective
    '$inj': 'INJUSDT',
    'inj': 'INJUSDT',
    'injective': 'INJUSDT',
    '#ustc': 'USTCUSDT', # TerraClassicUSD
    '$ustc': 'USTCUSDT',
    'ustc': 'USTCUSDT',
    'terraclassicusd': 'USTCUSDT',
    '#xter': 'XTERUSDT', # Alternatif zor
    '$xter': 'XTERUSDT',
    'xter': 'XTERUSDT',
    '#spec': 'SPECUSDT', # Alternatif zor
    '$spec': 'SPECUSDT',
    'spec': 'SPECUSDT',
    '#qi': 'QIUSDT', # BENQI
    '$qi': 'QIUSDT',
    'qi': 'QIUSDT',
    'benqi': 'QIUSDT',
    '#orca': 'ORCAUSDT', # Zaten tam adı
    '$orca': 'ORCAUSDT',
    'orca': 'ORCAUSDT',
    '#grass': 'GRASSUSDT', # GetGrass (points?)
    '$grass': 'GRASSUSDT',
    'grass': 'GRASSUSDT',
    'getgrass': 'GRASSUSDT',
    '#powr': 'POWRUSDT', # Powerledger
    '$powr': 'POWRUSDT',
    'powr': 'POWRUSDT',
    'powerledger': 'POWRUSDT',
    '#ip': 'IPUSDT', # Alternatif zor (IPVerse? Impossible Finance?)
    '$ip': 'IPUSDT',
    'ip': 'IPUSDT',
    '#pippin': 'PIPPINUSDT', # Alternatif zor
    '$pippin': 'PIPPINUSDT',
    'pippin': 'PIPPINUSDT',
    '#ilv': 'ILVUSDT', # Illuvium
    '$ilv': 'ILVUSDT',
    'ilv': 'ILVUSDT',
    'illuvium': 'ILVUSDT',
    '#cat': '1000CATUSDT', # Cat Token (CAT)
    '$cat': '1000CATUSDT',
    'cat': '1000CATUSDT',
    'cattoken': '1000CATUSDT',
    '#ban': 'BANUSDT', # Banano
    '$ban': 'BANUSDT',
    'ban': 'BANUSDT',
    'banano': 'BANUSDT',
    '#form': 'FORMUSDT', # Formation Fi
    '$form': 'FORMUSDT',
    'form': 'FORMUSDT',
    'formationfi': 'FORMUSDT',
}
