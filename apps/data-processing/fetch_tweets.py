import tweepy
import json
import pandas as pd
from config import TWITTER_BEARER_TOKEN

# Initialize Twitter API client
client = tweepy.Client(bearer_token=TWITTER_BEARER_TOKEN)

def fetch_tweets(keyword: str, count: int = 10):
    response = client.search_recent_tweets(query=keyword, tweet_fields=["created_at", "public_metrics"], max_results=count)
    
    tweets_data = []
    for tweet in response.data:
        tweets_data.append({
            "id": tweet.id,
            "text": tweet.text,
            "created_at": tweet.created_at,
            "retweets": tweet.public_metrics["retweet_count"],
            "likes": tweet.public_metrics["like_count"],
            "replies": tweet.public_metrics["reply_count"]
        })
    
    return tweets_data

if __name__ == "__main__":
    tweets = fetch_tweets("blockchain", 20)
    df = pd.DataFrame(tweets)
    df.to_csv("data/raw_tweets.csv", index=False)
    print("✅ Fetched tweets saved to raw_tweets.csv")
