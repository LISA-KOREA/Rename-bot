import os

class Config(object):

    TOKEN = os.environ.get("TOKEN", "")

    API_ID = int(os.environ.get("API_ID", ""))

    API_HASH = os.environ.get("API_HASH", "")

    DB_NAME = os.environ.get("DB_NAME","")

    DB_URL = os.environ.get("DB_URL","")

    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "")
