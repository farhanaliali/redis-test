import os
import time
import redis
from datetime import datetime

# Get Redis connection details from environment variables
REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
REDIS_PORT = os.getenv('REDIS_PORT', 6379)
REDIS_DB = os.getenv('REDIS_DB', 0)

# Initialize Redis connection
redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)

# Function to insert data into Redis
def insert_data_to_redis(data_key, data_value):
    redis_client.set(data_key, data_value)
    print(f"Data inserted: {data_key} = {data_value} at {datetime.now()}")

# Function to show data from Redis
def show_data_from_redis(data_key):
    data_value = redis_client.get(data_key)
    if data_value:
        print(f"Data fetched: {data_key} = {data_value.decode('utf-8')} at {datetime.now()}")
    else:
        print(f"No data found for key: {data_key} at {datetime.now()}")

# Main program with infinite loop
if __name__ == "__main__":
    data_id = 1  # Counter to give each entry a unique ID

    while True:
        # Insert new data into Redis
        data_key = f"data_{data_id}"
        data_value = f"example_data_{data_id}"
        insert_data_to_redis(data_key, data_value)

        # Show the inserted data from Redis
        show_data_from_redis(data_key)

        # Wait for 10 seconds before next iteration
        print(f"Waiting for 10 seconds at {datetime.now()}...\n")
        time.sleep(10)

        # Increment the ID for the next data entry
        data_id += 1
