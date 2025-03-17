import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_searcher')
API_ID = int(environ.get('API_ID', '20860011'))
API_HASH = environ.get('API_HASH', '8523438cd39e124dfe7038a1eb5b5873')
BOT_TOKEN = environ.get('BOT_TOKEN', '7802436962:AAHIV8KQ0hoJB6ITUUy19P6brkYKtirmfuU')

# Bot settings
AUTO_DEL = False
AUTO_DEL_TIME = int(300)
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = True 
PICS = (environ.get('PICS' ,'https://graph.org/file/df17e1fad3d856caf5df8.jpg https://graph.org/file/4db7c2e38f273e3b239dd.jpg https://graph.org/file/e4ead277c0bb7ab445c31.jpg https://graph.org/file/10d81181913c5d4237640.jpg https://graph.org/file/40fef09781fb9ded8cd13.jpg https://graph.org/file/b7b5a32ea575fa7ff50ee.jpg https://graph.org/file/bca1ca2c91828161aa247.jpg https://graph.org/file/bcea1a4ae0176d38a68b7.jpg https://graph.org/file/18a9f945534afa9db5036.jpg https://graph.org/file/89975fb3c157c1ae01e43.jpg https://graph.org/file/c548df4d4a42a8646aa04.jpg')).split()

# Admins, Channels & Users
OWNER_ID = environ.get('OWNER_ID', '7535513082')
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '7535513082 6350633297').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_grp = environ.get('AUTH_GROUP')
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_NAME = environ.get('DATABASE_NAME', "leo")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'leo_files')
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://flix1:flix1@cluster0.nkdcb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_URI2 = environ.get('DATABASE_URI2', "mongodb+srv://flix2:flix2@cluster0.yzov3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_URI3 = environ.get('DATABASE_URI3', "mongodb+srv://flix3:flix3@cluster0.zi1d5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# FSUB
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
# Set to False inside the bracket if you don't want to use Request Channel else set it to Channel ID
REQ_CHANNEL1=environ.get("REQ_CHANNEL1", None)
REQ_CHANNEL1 = (int(REQ_CHANNEL1) if REQ_CHANNEL1 and id_pattern.search(REQ_CHANNEL1) else False) if REQ_CHANNEL1 is not None else None
REQ_CHANNEL2 = environ.get("REQ_CHANNEL2", None)
REQ_CHANNEL2 = (int(REQ_CHANNEL2) if REQ_CHANNEL2 and id_pattern.search(REQ_CHANNEL2) else False) if REQ_CHANNEL2 is not None else None
JOIN_REQS_DB = environ.get("JOIN_REQS_DB", DATABASE_URI)
DELETE_TIMEOUT = int(environ.get('DELETE_TIMEOUT', 2*60*60)) # 2 hours in seconds

# Others
PM_DEL = int(300)

LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002392000389'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', '')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "<b>{file_caption}</b>")
BATCH_FILE_CAPTION = CUSTOM_FILE_CAPTION
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>Query: {query}</b> \n‌‌‌‌IMDb Data:\n\n🏷 Title: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Year: <a href={url}/releaseinfo>{year}</a>\n🌟 Rating: <a href={url}/ratings>{rating}</a> / 10")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "False")), False)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
