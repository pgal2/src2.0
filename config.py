import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8580917057:AAFUgaasKlrw0UucZoiRebkG1V_zxMm7-vc")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "29490954"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "dbd8f5af56b0f6e16327c20a84eece99")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "8327651421"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://fibegi:8oV4fjNNVasSfcoY@cluster0.jp8thup.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "idfinderpro")

# Force Subscription Channel
FORCE_SUB_CHANNEL = "idfinderpro"  # Channel username without @
FORCE_SUB_CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002441460670"))

# Log Channel - Set to 0 to disable logging
LOG_CHANNEL_ID = int(os.environ.get("LOG_CHANNEL_ID", "-1003689436454"))

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))

# Crypto Pay API Configuration (@CryptoBot / @send)
# Get your API token from https://t.me/CryptoBot?start=pay -> Create App
CRYPTO_PAY_API_TOKEN = os.environ.get("CRYPTO_PAY_API_TOKEN", "")  # Your Crypto Pay API token
CRYPTO_PAY_TESTNET = os.environ.get("CRYPTO_PAY_TESTNET", "False").lower() == "true"  # Set to True for testing with @CryptoTestnetBot