import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", ")
    API_HASH = os.environ.get("API_HASH", ")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", ")
    STRING_SESSION = os.environ.get("STRING_SESSION", "MM-5A-iQ5Jopq7qNV65P7ufk4ZemggPIyGrgMlfzKa73M2h0qrm8la-sqM5njFe267eQspyFc9x68cr5vKiQ81bc1pPkY_mR_FYxRdOd0kVSYG2x-AxTe8Q=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", True)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", ")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/3d8ecee0ba7dddfc6fce4.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", ") # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
