import requests
import time
from app.config import OPEN_EXCHANGE_API_KEY

BASE_URL = "https://openexchangerates.org/api/latest.json"

_cache = {"rates": None, "timestamp": 0}
CACHE_TTL = 3600  # 1 hour


def get_exchange_rates():
    if not OPEN_EXCHANGE_API_KEY:
        raise RuntimeError("API key not configured")

    # Use cached rates if still valid
    if _cache["rates"] and time.time() - _cache["timestamp"] < CACHE_TTL:
        return _cache["rates"]

    response = requests.get(
        BASE_URL,
        params={"app_id": OPEN_EXCHANGE_API_KEY},
        timeout=10
    )

    if response.status_code == 403:
        raise RuntimeError("Invalid or unauthorized API key")

    response.raise_for_status()
    data = response.json()

    _cache["rates"] = data["rates"]
    _cache["timestamp"] = time.time()

    return data["rates"]


def convert_currency(amount: float, from_currency: str, to_currency: str) -> float:
    rates = get_exchange_rates()

    if from_currency not in rates:
        raise ValueError(f"Unsupported currency: {from_currency}")

    if to_currency not in rates:
        raise ValueError(f"Unsupported currency: {to_currency}")

    # Convert via USD (OpenExchangeRates base currency)
    usd_amount = amount / rates[from_currency]
    converted = usd_amount * rates[to_currency]

    return converted
