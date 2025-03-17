import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

def get_db_connection():
    """Create and return a database connection."""
    try:
        conn = psycopg2.connect(DATABASE_URL)
        return conn
    except Exception as e:
        print(f"Database connection error: {e}")
        return None

def create_tables():
    """Create necessary tables in PostgreSQL."""
    conn = get_db_connection()
    if not conn:
        return
    
    query = """
    CREATE TABLE IF NOT EXISTS tweets (
        id SERIAL PRIMARY KEY,
        tweet_id VARCHAR(50) UNIQUE NOT NULL,
        username VARCHAR(50),
        content TEXT,
        created_at TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS onchain_data (
        id SERIAL PRIMARY KEY,
        tx_hash VARCHAR(66) UNIQUE NOT NULL,
        sender VARCHAR(50),
        receiver VARCHAR(50),
        amount NUMERIC,
        timestamp TIMESTAMP
    );
    """
    
    try:
        with conn.cursor() as cur:
            cur.execute(query)
            conn.commit()
    except Exception as e:
        print(f"Error creating tables: {e}")
    finally:
        conn.close()
