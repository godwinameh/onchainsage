from database import get_db_connection, create_tables
from fetch_tweets import fetch_tweets
from fetch_onchain import fetch_onchain_data
from clean_transform import clean_tweets, clean_onchain_data

def store_tweets(tweets):
    """Store tweets in the database."""
    conn = get_db_connection()
    if not conn:
        return

    query = "INSERT INTO tweets (tweet_id, username, content, created_at) VALUES (%s, %s, %s, %s) ON CONFLICT (tweet_id) DO NOTHING"

    try:
        with conn.cursor() as cur:
            for tweet in tweets:
                cur.execute(query, (tweet["tweet_id"], tweet["username"], tweet["content"], tweet["created_at"]))
            conn.commit()
    except Exception as e:
        print(f"Error inserting tweets: {e}")
    finally:
        conn.close()

def store_onchain_data(data):
    """Store blockchain transactions in the database."""
    conn = get_db_connection()
    if not conn:
        return

    query = "INSERT INTO onchain_data (tx_hash, sender, receiver, amount, timestamp) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (tx_hash) DO NOTHING"

    try:
        with conn.cursor() as cur:
            for tx in data:
                cur.execute(query, (tx["tx_hash"], tx["sender"], tx["receiver"], tx["amount"], tx["timestamp"]))
            conn.commit()
    except Exception as e:
        print(f"Error inserting blockchain data: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    create_tables()
    
    # Fetch, clean, and store tweets
    raw_tweets = fetch_tweets()
    cleaned_tweets = clean_tweets(raw_tweets)
    store_tweets(cleaned_tweets.to_dict(orient="records"))

    # Fetch, clean, and store on-chain data
    raw_onchain_data = fetch_onchain_data()
    cleaned_onchain_data = clean_onchain_data(raw_onchain_data)
    store_onchain_data(cleaned_onchain_data.to_dict(orient="records"))

    print(" Data ingestion completed successfully!")
