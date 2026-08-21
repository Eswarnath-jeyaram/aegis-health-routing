import json
import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    print("ERROR: MONGO_URI could not be loaded from .env file!")
    exit(1)

print("Connecting to MongoDB Atlas...")
client = MongoClient(MONGO_URI)
db = client["aegis_database"]
collection = db["hospitals"]

# Clear old data and seed
collection.delete_many({})

with open("data/hospitals.json", "r") as f:
    hospitals_data = json.load(f)

collection.insert_many(hospitals_data)
print(f"Successfully seeded {len(hospitals_data)} hospitals into MongoDB Atlas!")
