import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Twitter API Token
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_API_KEY")

# On-Chain API Key (Add this)
ONCHAIN_API_KEY = os.getenv("ONCHAIN_API_KEY")
