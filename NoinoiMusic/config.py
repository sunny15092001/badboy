# Thanks to Shikher, Levina, Bazibro.

from os import getenv

from dotenv import load_dotenv

load_dotenv()

que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSID = int(getenv("ASSID"))
ASSNAME = getenv("ASSNAME")
ASSUSERNAME = getenv("ASSUSERNAME")
BOT_ID = int(getenv("BOT_ID"))
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/TeamNoinoi/NoinoiMusic")
USERS = getenv("2056407064")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
MONGO_DB_URI = getenv("MONGO_DB_URI")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_ID = int(getenv("OWNER_ID"))
UPDATE = getenv("UPDATE")
SUPPORT = getenv("SUPPORT")
START_IMG = getenv("START_IMG")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "100"))
CMD_MUSIC = list(getenv("CMD_MUSIC", "/ !").split())
BG_IMG = getenv("BG_IMG", "https://telegra.ph/file/132e44742fac9e6ccd9f3.jpg")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5432635511").split()))
ASSISTANT_NAME = getenv("ASSNAME")
COMMAND_PREFIXES = ("/ ! .").split()
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/132e44742fac9e6ccd9f3.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/132e44742fac9e6ccd9f3.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/132e44742fac9e6ccd9f3.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/132e44742fac9e6ccd9f3.jpg")
