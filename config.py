# Copyright (c) 2025 devgagan : https://github.com/devgaganin.  
# Licensed under the GNU General Public License v3.0.  
# See LICENSE file in the repository root for full license text.

import os
from dotenv import load_dotenv

load_dotenv()

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

API_ID = os.getenv("API_ID", "20406918")
API_HASH = os.getenv("API_HASH", "45a7cdec1a4177ffde664c2639dfa20345a7cdec1a4177ffde664c2639dfa203")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7664317188:AAFZMREj_PGdAgvHvl9H1JXMxirIfQMLjXY")
MONGO_DB = os.getenv("MONGO_DB", "mongodb+srv://telegram:telegram@telegram.gcohn4c.mongodb.net/?retryWrites=true&w=majority&appName=Telegram")
OWNER_ID = list(map(int, os.getenv("OWNER_ID", "1237373354").split())) # list seperated via space
DB_NAME = os.getenv("DB_NAME", "telegram_downloader")
STRING = os.getenv("STRING", None) # optional
LOG_GROUP = int(os.getenv("LOG_GROUP", "-1001234456")) # optional with -100
FORCE_SUB = int(os.getenv("FORCE_SUB", "-10012345567")) # optional with -100
MASTER_KEY = os.getenv("MASTER_KEY", "gK8HzLfT9QpViJcYeB5wRa3DmN7P2xUq") # for session encryption
IV_KEY = os.getenv("IV_KEY", "s7Yx5CpVmE3F") # for decryption
YT_COOKIES = os.getenv("YT_COOKIES", YTUB_COOKIES)
INSTA_COOKIES = os.getenv("INSTA_COOKIES", INST_COOKIES)
FREEMIUM_LIMIT = int(os.getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(os.getenv("PREMIUM_LIMIT", "500"))
