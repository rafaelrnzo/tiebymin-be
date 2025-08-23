from typing import Optional
from google.oauth2 import id_token
from google.auth.transport import requests
from app.core.config import settings
import logging

def verify_google_token(token: str):
    try:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), None)
        return idinfo
    except ValueError as e:
        logging.error(f"Google token verification failed: {e}")
        return None
    except Exception as e:
        logging.error(f"Unexpected error during Google token verification: {e}")
        return None
