import requests
import pandas as pd
from config import ONCHAIN_API_KEY

def fetch_onchain_data():
    url = f"https://api.onchain.com/transactions?apikey={ONCHAIN_API_KEY}"
    response = requests.get(url)
    data = response.json()
    
    transactions = [
        {
            "tx_id": tx["id"],
            "timestamp": tx["timestamp"],
            "value": tx["value"],
            "from": tx["from"],
            "to": tx["to"]
        }
        for tx in data["transactions"]
    ]
    
    return transactions

if __name__ == "__main__":
    onchain_data = fetch_onchain_data()
    df = pd.DataFrame(onchain_data)
    df.to_csv("data/raw_onchain.csv", index=False)
    print("✅ Fetched on-chain data saved to raw_onchain.csv")
