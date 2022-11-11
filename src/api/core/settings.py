import os


try:
    from dotenv import load_dotenv
    
    load_dotenv()
    
except ImportError:
    pass


FAVICON_API = "https://favicongrabber.com/api/grab"

APP_URL = os.getenv('DETA_SPACE_APP_HOSTNAME')