import os


try:
    from dotenv import load_dotenv
    
    load_dotenv()
    
except ImportError:
    pass


FAVICON_API = "https://favicongrabber.com/api/grab"

APP_URL = os.getenv('DETA_SPACE_APP_HOSTNAME')

JWT_SECRET = os.getenv("APP_SECRET", "489F5CE81A2BEA4E93B97CF4A2857")
JWT_ALGORITHM = "HS256"