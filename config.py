#(©)CodeXBotz

import os  # Import the 'os' module
import logging  # Import the 'logging' module
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv()

# Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

# Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", ""))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

# Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", ""))

# Port
PORT = os.environ.get("PORT", "8080")

# Database 
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

# Force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))
FORCE_SUB_CHANNEL_2 = int(os.environ.get("FORCE_SUB_CHANNEL_2", "0"))  # New force sub channel

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Start message
START_PIC = os.environ.get("START_PIC","")
START_MSG = os.environ.get("START_MESSAGE", "𝐇𝐞𝐥𝐥𝐨 <b>{first}</b> 🤝🤝\n\n 𝐓𝐡𝐢𝐬 𝐢𝐬 𝐚𝐧 𝐋-𝐅𝐋𝐈𝐗 𝐬𝐩𝐞𝐜𝐢𝐚𝐥 𝐛𝐨𝐭 𝐰𝐡𝐢𝐜𝐡 𝐬𝐭𝐨𝐫𝐞𝐬 𝐟𝐢𝐥𝐞𝐬 𝐢𝐧 𝐬𝐩𝐞𝐜𝐢𝐟𝐢𝐜 𝐜𝐡𝐚𝐧𝐧𝐞𝐥 𝐚𝐧𝐝 𝐮𝐬𝐞𝐫𝐬 𝐚𝐜𝐜𝐞𝐬𝐬 𝐭𝐡𝐞𝐦 𝐟𝐫𝐨𝐦 𝐚 𝐬𝐩𝐞𝐜𝐢𝐚𝐥 𝐥𝐢𝐧𝐤")

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")

# Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "𝐇𝐞𝐥𝐥𝐨 {first} 🤝🤝 \n\n<b>𝒀𝒐𝒖 𝒏𝒆𝒆𝒅 𝒕𝒐 𝒋𝒐𝒊𝒏 𝑳-𝑭𝑳𝑰𝑿 𝑺𝒖𝒑𝒑𝒐𝒓𝒕 𝑮𝒓𝒐𝒖𝒑 𝒂𝒏𝒅 𝑪𝒉𝒂𝒏𝒏𝒆𝒍 𝒊𝒏 𝒐𝒓𝒅𝒆𝒓 𝒕𝒐 𝒖𝒔𝒆 𝒎𝒆\n\n𝑷𝒍𝒆𝒂𝒔𝒆 𝒋𝒐𝒊𝒏 𝒕𝒉𝒆 𝒈𝒓𝒐𝒖𝒑 𝒂𝒏𝒅 𝒄𝒉𝒂𝒏𝒏𝒆𝒍 𝒃𝒚 𝒇𝒐𝒍𝒍𝒐𝒘𝒊𝒏𝒈 𝒕𝒉𝒆 𝒍𝒊
