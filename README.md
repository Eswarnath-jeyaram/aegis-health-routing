# AegisLink: Health Referral Optimizer 🚑

AegisLink is a cloud-native, deterministic optimization engine designed to eliminate blind medical referrals. By cross-referencing real-time hospital bed capacity with exact clinical requirements and OSRM-calculated drive times, AegisLink routes emergency ambulances to the optimal medical facility in milliseconds.

Built as an engineering experience during a 24-hour hackathon, this platform bridges complex algorithmic sorting with an accessible, high-speed dispatch dashboard.

## 🚀 Live Deployment
* **Frontend (Vercel):** `https://aegis-health-routing.vercel.app/`

## 🛠️ Tech Stack
* **Frontend:** HTML, CSS, JavaScript, Leaflet.js (Hosted on Vercel)
* **Backend:** Python, FastAPI (Hosted on Render)
* **Database:** MongoDB (Real-time spatial & inventory data)
* **Routing Algorithm:** Open Source Routing Machine (OSRM) with Contraction Hierarchies

## 📁 Repository Structure
```text
aegis-health-routing/
├── app/
│   ├── __init__.py
│   ├── engine.py        # Core deterministic optimization math
│   └── main.py          # FastAPI server and route handlers
├── data/
│   ├── add_data.py      # Script to populate database
│   ├── hospitals.json   # Mock inventory dataset
│   └── patient_request.json 
├── frontend/
│   ├── index.html       # Dispatcher dashboard & Leaflet map UI
│   └── requirements.txt 
├── .env                 # Environment variables (MongoDB URI)
├── .gitignore
├── requirements.txt     # Backend Python dependencies
└── seed.py              # Cloud database initialization script

```

## ⚙️ Local Setup & Installation

If you want to run AegisLink locally, follow these steps to clone and launch the environment.

### 1. Clone the Repository

```bash
git clone [https://github.com/YOUR_GITHUB_USERNAME/aegis-health-routing.git](https://github.com/YOUR_GITHUB_USERNAME/aegis-health-routing.git)
cd aegis-health-routing

```

### 2. Set Up the Backend Environment

Ensure you have Python 3.8+ installed. Install the required dependencies:

```bash
pip install -r requirements.txt

```

### 3. Configure the Database

Create a `.env` file in the root directory and add your MongoDB connection string:

```text
MONGODB_URI="mongodb+srv://<username>:<password>@cluster.mongodb.net/?retryWrites=true&w=majority"

```

### 4. Seed the Database

Populate your MongoDB instance with the initial hospital network and inventory data:

```bash
python seed.py

```

### 5. Run the Backend Server

Launch the FastAPI application locally using Uvicorn:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

```

The API will now be running at `http://localhost:8000`.

### 6. Launch the Frontend

Since the frontend is pure HTML/JS, you can simply open the `frontend/index.html` file in any modern web browser, or serve it using a basic Python HTTP server:

```bash
cd frontend
python -m http.server 3000

```

Navigate to `http://localhost:3000` to view the live dashboard.

## 🧠 Core Algorithmic Logic

AegisLink relies on a custom **Multi-Criteria Weighted Optimization** algorithm (`engine.py`).

1. **Filtering:** Instantly removes hospitals that lack the required specialist or have 0 requested beds.
2. **Weighting:** Assigns a deterministic score balancing available resource capacity against total drive time.
3. **Pathfinding:** Integrates OSRM to calculate the true road-network drive time rather than simple linear GPS distance.

```

***

### How to use this:
1. Paste the text above into your `README.md` file[cite: 4].
2. Replace `YOUR_GITHUB_USERNAME` with your actual username.
3. Once you deploy on Vercel and Render using the steps we discussed earlier, copy those generated URLs and paste them into the `[INSERT_YOUR_..._LINK_HERE]` slots at the very top. 

This makes your repository look polished, professional, and ready for any technical judge to review!

```
