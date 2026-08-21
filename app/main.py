from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
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

@app.get("/")
def read_root():
    return {"status": "AegisLink Cloud Engine is Online", "database": "MongoDB Atlas"}

@app.get("/hospitals")
def get_hospitals_endpoint():
    """Fetch all active hospitals from MongoDB."""
    hospitals = get_all_hospitals()
    return {"hospitals": hospitals}

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
