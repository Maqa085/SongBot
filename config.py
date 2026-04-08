from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "0")) # .env-ə əlavə et
API_HASH = getenv("API_HASH")       # .env-ə əlavə et
BOT_TOKEN = getenv("BOT_TOKEN")
