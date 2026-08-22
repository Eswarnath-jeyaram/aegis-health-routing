import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from the root .env file
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    raise ValueError("CRITICAL ERROR: MONGO_URI environment variable is missing or empty!")

# Connect to MongoDB Atlas
client = MongoClient(MONGO_URI)
db = client["aegis_database"]
hospitals_collection = db["hospitals"]

def get_all_hospitals():
    """Fetch all hospitals from MongoDB Atlas, excluding the internal MongoDB _id field."""
    hospitals = list(hospitals_collection.find({}, {"_id": 0}))
    return hospitals

def update_hospital_capacity(hospital_id: str, icu_delta: int = 1, vent_delta: int = 1):
    """Atomically decrease hospital resources ONLY if capacity exists."""
    
    # We add a filter checking that current beds are greater than or equal to ($gte) the requested beds
    result = hospitals_collection.update_one(
        {
            "id": hospital_id,
            "available_icu": {"$gte": icu_delta},
            "available_ventilators": {"$gte": vent_delta}
        },
        {
            "$inc": {
                "available_icu": -icu_delta,
                "available_ventilators": -vent_delta
            }
        }
    )
    
    # If the hospital didn't have enough beds, modified_count will be 0 (False)
    return result.modified_count > 0
