# By @TroJanzHEX


import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("6078574846:AAFHx-5f-Mrz8At2pFxPn8ZpUx7uffjngSw", "")

    APP_ID = int(os.environ.get("27535343", 12345))

    API_HASH = os.environ.get("06766128d68d9c1a0d683ecfbb91de2f", "")

    # Get this api from https://www.remove.bg/b/background-removal-api
    RemoveBG_API = os.environ.get("cg7YwVEpvDTGEUVuJK9yaxtS", "")
