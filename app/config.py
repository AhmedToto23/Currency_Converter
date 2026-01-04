from dotenv import load_dotenv
import os

load_dotenv()

OPEN_EXCHANGE_API_KEY = os.getenv("OPEN_EXCHANGE_API_KEY")

BASE_URL = "https://openexchangerates.org/api/latest.json"

if not OPEN_EXCHANGE_API_KEY:
    raise RuntimeError("OPEN_EXCHANGE_API_KEY is not set")
