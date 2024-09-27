from os import getenv

class Config(object):
      API_HASH = getenv("e2e9b22c6522465b62d8445840a526b1")
      API_ID = int(getenv("8143727"))
      AS_COPY = True if getenv("True") == "`{file_name}`" else True
      BOT_TOKEN = "7906300237:AAE0ck3P7BKZMkFROZnY9GLjZdgXmMVt7d0"
      session_string = getenv("session_string", "")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1002369069695:-1002252994329").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
