import math
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from app.engine import get_all_hospitals, update_hospital_capacity

app = FastAPI(title="AegisLink Backend", version="2.0")

# Enable CORS so your frontend can communicate with this server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RouteRequest(BaseModel):
    hospital_id: str
    icu_count: int = 1
    ventilator_count: int = 1

class OptimizeRequest(BaseModel):
    patient_lat: float
    patient_lon: float
    required_icu: int = 1
    required_vent: int = 1

def calculate_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Calculate the Great-Circle distance in kilometers using the Haversine formula."""
    r = 6371.0  # Earth radius in kilometers
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return r * c

@app.get("/")
def read_root():
    return {"status": "AegisLink Cloud Engine is Online", "database": "MongoDB Atlas"}

@app.get("/hospitals")
def get_hospitals_endpoint():
    """Fetch all active hospitals from MongoDB."""
    hospitals = get_all_hospitals()
    return {"hospitals": hospitals}

@app.post("/optimize")
def optimize_referral(request: OptimizeRequest):
    """Find the nearest hospital matching the required ICU and ventilator capacity."""
    hospitals = get_all_hospitals()
    
    eligible = []
    for h in hospitals:
        avail_icu = h.get("available_icu") or (h.get("capacity", {}).get("icu_beds", 0)) or 0
        avail_vent = h.get("available_vent") or (h.get("capacity", {}).get("ventilators", 0)) or 0
        
        if avail_icu >= request.required_icu and avail_vent >= request.required_vent:
            h_lat = h.get("latitude") or h.get("lat")
            h_lon = h.get("longitude") or h.get("lon")
            
            if h_lat is not None and h_lon is not None:
                dist = calculate_distance(request.patient_lat, request.patient_lon, float(h_lat), float(h_lon))
                eligible.append({**h, "distance_km": round(dist, 2)})

    if not eligible:
        raise HTTPException(
            status_code=404, 
            detail="No hospitals found with the requested ICU/Ventilator capacity."
        )

    # Sort by straight-line distance
    eligible.sort(key=lambda x: x["distance_km"])
    return {"optimal_hospital": eligible[0], "all_eligible": eligible}

@app.post("/route")
def route_ambulance(request: RouteRequest):
    """Handle emergency routing and decrement live hospital capacity."""
    success = update_hospital_capacity(
        request.hospital_id, 
        request.icu_count, 
        request.ventilator_count
    )
    if not success:
        raise HTTPException(status_code=404, detail="Hospital not found or update failed")
    
    return {
        "status": "success", 
        "message": f"Successfully routed to hospital {request.hospital_id}. Capacities updated."
    }
