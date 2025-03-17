import pandas as pd

def clean_tweets(raw_tweets):
    """Clean and transform tweets data."""
    df = pd.DataFrame(raw_tweets)
    
    if 'text' in df.columns:
        df = df.rename(columns={"text": "content", "id": "tweet_id"})
        df["content"] = df["content"].str.replace(r"http\S+", "", regex=True)  # Remove URLs
    return df

def clean_onchain_data(raw_data):
    """Clean and transform blockchain data."""
    df = pd.DataFrame(raw_data)
    
    if 'hash' in df.columns:
        df = df.rename(columns={"hash": "tx_hash", "from": "sender", "to": "receiver", "value": "amount"})
    return df
