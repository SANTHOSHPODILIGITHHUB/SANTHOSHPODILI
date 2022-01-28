from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "8391805"))
API_HASH = getenv("API_HASH", "2f10c7db9aa6c58d1a410c2cb7b3aeb5")
BOT_TOKEN = getenv("BOT_TOKEN", "5122625103:AAFzQysPcE0VC7cDRDpJPPihLS31ZOm4rMQ")