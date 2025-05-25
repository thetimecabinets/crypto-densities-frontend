import requests
import json
from datetime import datetime

# --- Fear & Greed Index ---
try:
    res = requests.get("https://api.alternative.me/fng/")
    fng = res.json()["data"][0]
    fear_data = {
        "value": fng["value"],
        "status": fng["value_classification"],
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }
    with open("data/fear-greed.json", "w") as f:
        json.dump(fear_data, f, indent=2)
except Exception as e:
    print("Failed to update fear-greed.json:", e)

# --- Top 10 Momentum (from CoinGecko) ---
try:
    res = requests.get("https://api.coingecko.com/api/v3/coins/markets", params={
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 10,
        "page": 1,
        "price_change_percentage": "24h"
    })
    data = res.json()
    coins = []
    for coin in data:
        coins.append({
            "name": coin["symbol"].upper(),
            "price": coin["current_price"],
            "change": coin["price_change_percentage_24h"]
        })
    with open("data/momentum.json", "w") as f:
        json.dump(coins, f, indent=2)
except Exception as e:
    print("Failed to update momentum.json:", e)
