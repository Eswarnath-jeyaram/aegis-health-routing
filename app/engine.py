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

def update_hospital_capacity(hospital_id: str, icu_delta: int = 1, vent_delta: int = 1, general_delta: int = 0):
    """Atomically decrease hospital resources ONLY if capacity exists."""
    
    # FIX: Pointed the filters to the nested 'capacity' fields from your database schema
    # FIX: Added 'general_beds' to the filter and increment logic
    result = hospitals_collection.update_one(
        {
            "id": hospital_id,
            "capacity.icu_beds": {"$gte": icu_delta},
            "capacity.ventilators": {"$gte": vent_delta},
            "capacity.general_beds": {"$gte": general_delta}
        },
        {
            "$inc": {
                "capacity.icu_beds": -icu_delta,
                "capacity.ventilators": -vent_delta,
                "capacity.general_beds": -general_delta
            }
        }
    )
    
    # If the hospital didn't have enough beds, modified_count will be 0 (False)
    return result.modified_count > 0
