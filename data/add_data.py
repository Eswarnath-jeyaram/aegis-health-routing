import sys
from pymongo import MongoClient

# ==========================================
# Phase 1: SET YOUR CONNECTION
# ==========================================
# Added the WSL TLS bypass flag to the end of your specific link!
MONGO_URI = "mongodb+srv://eswarnathj_db_user:Aegis1234@aegisdata.cifvhwa.mongodb.net/?appName=aegisdata&tlsAllowInvalidCertificates=true"

def get_hospital_collection():
    """Connects to MongoDB and returns the 'hospitals' collection."""
    try:
        client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
        client.admin.command('ping')
        
        # Explicitly target the exact database name
        db = client["aegis_database"]
        
        print(f"✅ Connected successfully to Database: {db.name}")
        return db.get_collection("hospitals")
        
    except Exception as e:
        # If it fails, this will now print the REAL, detailed error from the system
        print(f"🛑 EXACT ERROR: {e}")
        sys.exit(1)

# ========================================================
# Phase 2: ALL 100 FULLY PARAMETERIZED CHENNAI HOSPITALS
# ========================================================
NEW_HOSPITALS = [
    {"id": "H001", "name": "Rajiv Gandhi Government General Hospital", "lat": 13.0815, "lon": 80.2765, "capacity": {"icu_beds": 80, "general_beds": 500, "ventilators": 45}, "resources": ["Trauma_Surgeon", "CT_Scanner", "MRI", "ICU_Ventilator", "Oxygen_Pipeline_System", "Cath_Lab", "Medical_Oxygen_Plant"]},
    {"id": "H002", "name": "Apollo Hospitals, Greams Road", "lat": 13.0617, "lon": 80.2522, "capacity": {"icu_beds": 70, "general_beds": 350, "ventilators": 40}, "resources": ["Cardiology", "Cath_Lab", "MRI", "3T_MRI", "PET-CT", "Linear_Accelerator", "Oxygen_Pipeline_System"]},
    {"id": "H003", "name": "MIOT International, Manapakkam", "lat": 13.0135, "lon": 80.1764, "capacity": {"icu_beds": 60, "general_beds": 300, "ventilators": 35}, "resources": ["Orthopedics", "Trauma_Surgeon", "1.5T_MRI", "Arthroscopy_System", "Blood_Bank_Refrigerator", "Hemodialysis_Machine"]},
    {"id": "H004", "name": "Sri Ramachandra Medical Centre, Porur", "lat": 13.0371, "lon": 80.1472, "capacity": {"icu_beds": 75, "general_beds": 400, "ventilators": 40}, "resources": ["Emergency_Medicine", "Trauma_Surgeon", "Neonatology", "CT_Scanner", "CRRT_Machine", "Oxygen_Pipeline_System"]},
    {"id": "H005", "name": "Kauvery Hospital, Alwarpet", "lat": 13.0336, "lon": 80.2560, "capacity": {"icu_beds": 40, "general_beds": 180, "ventilators": 20}, "resources": ["Cardiology", "Cath_Lab", "Echocardiography", "Defibrillator", "Oxygen_Pipeline_System"]},
    {"id": "H006", "name": "SIMS Hospital, Vadapalani", "lat": 13.0526, "lon": 80.2100, "capacity": {"icu_beds": 50, "general_beds": 250, "ventilators": 25}, "resources": ["Trauma_Surgeon", "Burn_Unit", "Plastic_Surgery", "Surgical_Microscope", "ICU_Ventilator"]},
    {"id": "H007", "name": "Fortis Malar Hospital, Adyar", "lat": 13.0125, "lon": 80.2575, "capacity": {"icu_beds": 35, "general_beds": 160, "ventilators": 18}, "resources": ["Cardiothoracic_Surgery", "Cath_Lab", "Multiparameter_Monitor", "Blood_Bank_Refrigerator"]},
    {"id": "H008", "name": "Gleneagles Global Health City, Perumbakkam", "lat": 12.9056, "lon": 80.1983, "capacity": {"icu_beds": 70, "general_beds": 350, "ventilators": 35}, "resources": ["Transplant_Surgeon", "Hepatology", "3T_MRI", "CRRT_Machine", "Medical_Oxygen_Plant"]},
    {"id": "H009", "name": "Dr. Rela Institute & Medical Centre, Chromepet", "lat": 12.9610, "lon": 80.1417, "capacity": {"icu_beds": 65, "general_beds": 300, "ventilators": 30}, "resources": ["Transplant_Surgeon", "Neonatal_Ventilator", "Neonatal_Incubator", "Radiant_Warmer", "Oxygen_Pipeline_System"]},
    {"id": "H010", "name": "MGM Healthcare, Aminjikarai", "lat": 13.0725, "lon": 80.2223, "capacity": {"icu_beds": 50, "general_beds": 250, "ventilators": 25}, "resources": ["Cardiology", "PET-CT", "Cath_Lab", "Anesthesia_Machine", "Oxygen_Pipeline_System"]},
    {"id": "H011", "name": "Government Stanley Medical College", "lat": 13.1092, "lon": 80.2831, "capacity": {"icu_beds": 80, "general_beds": 600, "ventilators": 40}, "resources": ["Burn_Unit", "Trauma_Surgeon", "Medical_Oxygen_Plant", "Blood_Bank_Refrigerator"]},
    {"id": "H012", "name": "Chettinad Health City, Kelambakkam", "lat": 12.8123, "lon": 80.2201, "capacity": {"icu_beds": 50, "general_beds": 280, "ventilators": 24}, "resources": ["CT_Scanner", "ICU_Ventilator", "Oxygen_Pipeline_System", "Internal_Medicine"]},
    {"id": "H013", "name": "Vijaya Hospital, Vadapalani", "lat": 13.0487, "lon": 80.2079, "capacity": {"icu_beds": 40, "general_beds": 200, "ventilators": 20}, "resources": ["Gastroenterology", "Upper_GI_Endoscope", "Colonoscope", "Digital_X-Ray"]},
    {"id": "H014", "name": "Billroth Hospitals, Shenoy Nagar", "lat": 13.0782, "lon": 80.2265, "capacity": {"icu_beds": 30, "general_beds": 150, "ventilators": 15}, "resources": ["Cath_Lab", "ICU_Ventilator", "Digital_X-Ray", "Ultrasound_Machine"]},
    {"id": "H015", "name": "Apollo Proton Cancer Centre, Taramani", "lat": 12.9818, "lon": 80.2458, "capacity": {"icu_beds": 40, "general_beds": 200, "ventilators": 20}, "resources": ["Oncology", "Linear_Accelerator", "Brachytherapy_Unit", "PET-CT", "Chemotherapy_Infusion_Pump"]},
    {"id": "H016", "name": "Government Kilpauk Medical College Hospital", "lat": 13.0785, "lon": 80.2415, "capacity": {"icu_beds": 60, "general_beds": 400, "ventilators": 30}, "resources": ["Burn_Unit", "Emergency_Medicine", "Digital_X-Ray", "Oxygen_Pipeline_System"]},
    {"id": "H017", "name": "Government Multi Super Speciality Hospital, Omandurar", "lat": 13.0585, "lon": 80.2700, "capacity": {"icu_beds": 90, "general_beds": 500, "ventilators": 50}, "resources": ["Trauma_Surgeon", "Neurosurgery", "3T_MRI", "Cath_Lab", "Medical_Oxygen_Plant"]},
    {"id": "H018", "name": "Dr. Mehta's Hospitals, Chetpet", "lat": 13.0750, "lon": 80.2420, "capacity": {"icu_beds": 35, "general_beds": 160, "ventilators": 16}, "resources": ["Neonatology", "Neonatal_Incubator", "Phototherapy_Unit", "Oxygen_Pipeline_System"]},
    {"id": "H019", "name": "St. Isabel's Hospital, Mylapore", "lat": 13.0330, "lon": 80.2680, "capacity": {"icu_beds": 25, "general_beds": 130, "ventilators": 12}, "resources": ["General_Surgery", "Blood_Bank_Refrigerator", "Digital_X-Ray"]},
    {"id": "H020", "name": "Sundaram Medical Foundation, Anna Nagar", "lat": 13.0850, "lon": 80.2100, "capacity": {"icu_beds": 30, "general_beds": 150, "ventilators": 15}, "resources": ["Internal_Medicine", "Ultrasound_Machine", "Hematology_Analyzer", "Oxygen_Pipeline_System"]},
    {"id": "H021", "name": "Prashanth Super Speciality Hospital, Velachery", "lat": 12.9818, "lon": 80.2185, "capacity": {"icu_beds": 28, "general_beds": 140, "ventilators": 14}, "resources": ["Obstetrics_&_Gynecology", "Obstetric_Ultrasound", "Fetal_Monitor_CTG", "Trauma_Surgeon"]},
    {"id": "H022", "name": "Madras Medical Mission, Mogappair", "lat": 13.0834, "lon": 80.1920, "capacity": {"icu_beds": 55, "general_beds": 250, "ventilators": 28}, "resources": ["Cardiology", "Cath_Lab", "Echocardiography", "Oxygen_Pipeline_System"]},
    {"id": "H023", "name": "Apollo Speciality Hospital, Vanagaram", "lat": 13.0730, "lon": 80.1650, "capacity": {"icu_beds": 50, "general_beds": 240, "ventilators": 25}, "resources": ["Trauma_Surgeon", "Cath_Lab", "CT_Scanner", "Emergency_Medicine"]},
    {"id": "H024", "name": "SRM General Hospital, Kattankulathur", "lat": 12.8231, "lon": 80.0444, "capacity": {"icu_beds": 60, "general_beds": 350, "ventilators": 30}, "resources": ["Trauma_Surgeon", "Hemodialysis_Machine", "Blood_Bank_Refrigerator", "Digital_X-Ray"]},
    {"id": "H025", "name": "Meenakshi Mission Hospital", "lat": 13.1431, "lon": 79.9085, "capacity": {"icu_beds": 30, "general_beds": 160, "ventilators": 15}, "resources": ["Trauma_Surgeon", "Oxygen_Pipeline_System", "Blood_Bank_Refrigerator"]},
    {"id": "H026", "name": "Tagore Medical College and Hospital", "lat": 12.8642, "lon": 80.1321, "capacity": {"icu_beds": 35, "general_beds": 200, "ventilators": 16}, "resources": ["General_Surgery", "Digital_X-Ray", "ICU_Ventilator"]},
    {"id": "H027", "name": "Annai Arul Hospital, Mudichur", "lat": 12.9321, "lon": 80.1054, "capacity": {"icu_beds": 22, "general_beds": 100, "ventilators": 10}, "resources": ["Trauma_Surgeon", "Ultrasound_Machine", "Oxygen_Pipeline_System"]},
    {"id": "H028", "name": "Kanchi Kamakoti CHILDS Trust Hospital", "lat": 13.0550, "lon": 80.2420, "capacity": {"icu_beds": 45, "general_beds": 180, "ventilators": 22}, "resources": ["Pediatrics", "Paediatric_ICU", "Neonatal_Incubator", "Neonatal_Ventilator"]},
    {"id": "H029", "name": "Venkateswara Hospitals, Nandanam", "lat": 13.0280, "lon": 80.2450, "capacity": {"icu_beds": 25, "general_beds": 120, "ventilators": 12}, "resources": ["MRI", "Blood_Bank_Refrigerator", "Oxygen_Pipeline_System"]},
    {"id": "H030", "name": "Aakash Hospital, Velachery", "lat": 12.9750, "lon": 80.2210, "capacity": {"icu_beds": 20, "general_beds": 90, "ventilators": 8}, "resources": ["Emergency_Medicine", "Digital_X-Ray", "Trauma_Surgeon"]},
    {"id": "H031", "name": "Srushti Hospital, Ramapuram", "lat": 13.0250, "lon": 80.1820, "capacity": {"icu_beds": 15, "general_beds": 70, "ventilators": 6}, "resources": ["Obstetrics_&_Gynecology", "Ultrasound_Machine", "Infertility_IVF_Equipment"]},
    {"id": "H032", "name": "New Life Hospital, Tambaram", "lat": 12.9245, "lon": 80.1270, "capacity": {"icu_beds": 18, "general_beds": 85, "ventilators": 8}, "resources": ["Digital_X-Ray", "Oxygen_Pipeline_System"]},
    {"id": "H033", "name": "COMET Hospital, Medavakkam", "lat": 12.9230, "lon": 80.1850, "capacity": {"icu_beds": 20, "general_beds": 95, "ventilators": 9}, "resources": ["Blood_Bank_Refrigerator", "Oxygen_Pipeline_System"]},
    {"id": "H034", "name": "Global Hospital Outpatient Center, Egmore", "lat": 13.0800, "lon": 80.2600, "capacity": {"icu_beds": 25, "general_beds": 120, "ventilators": 12}, "resources": ["CT_Scanner", "MRI", "Diagnostic_Imaging"]},
    {"id": "H035", "name": "Apollo Clinic & Day Care, Velachery", "lat": 12.9700, "lon": 80.2200, "capacity": {"icu_beds": 12, "general_beds": 60, "ventilators": 5}, "resources": ["CT_Scanner", "Digital_X-Ray", "Ultrasound_Machine"]},
    {"id": "H036", "name": "Lifeline Hospitals, Kilpauk", "lat": 13.0820, "lon": 80.2380, "capacity": {"icu_beds": 30, "general_beds": 140, "ventilators": 14}, "resources": ["Trauma_Surgeon", "Blood_Bank_Refrigerator", "ICU_Ventilator"]},
    {"id": "H037", "name": "Government Royapettah Hospital", "lat": 13.0500, "lon": 80.2600, "capacity": {"icu_beds": 35, "general_beds": 160, "ventilators": 16}, "resources": ["Burn_Unit", "Trauma_Surgeon", "Orthopedics", "Neurology"]},
    {"id": "H038", "name": "Sooriya Hospital, Vadapalani", "lat": 13.0490, "lon": 80.2120, "capacity": {"icu_beds": 28, "general_beds": 130, "ventilators": 12}, "resources": ["MRI", "Oxygen_Pipeline_System", "Blood_Bank_Refrigerator"]},
    {"id": "H039", "name": "C.S.I. Kalyani Hospital, Mylapore", "lat": 13.0380, "lon": 80.2650, "capacity": {"icu_beds": 22, "general_beds": 110, "ventilators": 10}, "resources": ["General_Surgery", "Internal_Medicine", "Blood_Bank_Refrigerator"]},
    {"id": "H040", "name": "Government Hospital for Thoracic Medicine, Tambaram", "lat": 12.9350, "lon": 80.1380, "capacity": {"icu_beds": 50, "general_beds": 500, "ventilators": 25}, "resources": ["Pulmonology", "Bronchoscope", "Spirometer", "Medical_Oxygen_Plant"]},
    {"id": "H041", "name": "Hindu Mission Hospital, Tambaram", "lat": 12.9239, "lon": 80.1147, "capacity": {"icu_beds": 30, "general_beds": 200, "ventilators": 12}, "resources": ["Trauma_Surgeon", "General_Surgery", "Dialysis_Water_Treatment_System", "Oxygen_Pipeline_System"]},
    {"id": "H042", "name": "Parvathy Hospital, Chromepet", "lat": 12.9515, "lon": 80.1415, "capacity": {"icu_beds": 40, "general_beds": 150, "ventilators": 20}, "resources": ["Orthopedics", "Joint_Replacement_Surgical_Instruments", "Trauma_Surgeon", "C-Arm", "Digital_X-Ray"]},
    {"id": "H043", "name": "Balaji Hospital, Guindy", "lat": 13.0075, "lon": 80.2185, "capacity": {"icu_beds": 20, "general_beds": 120, "ventilators": 10}, "resources": ["Internal_Medicine", "Emergency_Medicine", "Blood_Bank_Refrigerator"]},
    {"id": "H044", "name": "VHM Hospital, Saligramam", "lat": 13.0566, "lon": 80.1982, "capacity": {"icu_beds": 15, "general_beds": 80, "ventilators": 5}, "resources": ["General_Surgery", "Ultrasound_Machine", "Patient_Monitor"]},
    {"id": "H045", "name": "KHM Hospital, Anna Nagar", "lat": 13.0881, "lon": 80.2123, "capacity": {"icu_beds": 18, "general_beds": 90, "ventilators": 6}, "resources": ["Pediatrics", "Obstetrics_&_Gynecology", "Fetal_Monitor_CTG"]},
    {"id": "H046", "name": "Be Well Hospital, Kilpauk", "lat": 13.0805, "lon": 80.2405, "capacity": {"icu_beds": 20, "general_beds": 100, "ventilators": 8}, "resources": ["Emergency_Medicine", "Defibrillator", "Oxygen_Pipeline_System"]},
    {"id": "H047", "name": "B.R.S Hospital, Nungambakkam", "lat": 13.0601, "lon": 80.2456, "capacity": {"icu_beds": 25, "general_beds": 110, "ventilators": 10}, "resources": ["Internal_Medicine", "Digital_X-Ray", "Biochemistry_Analyzer"]},
    {"id": "H048", "name": "Saraswathy Multispeciality Hospital, Madipakkam", "lat": 12.9641, "lon": 80.1970, "capacity": {"icu_beds": 16, "general_beds": 75, "ventilators": 7}, "resources": ["Orthopedics", "Physical_Medicine_&_Rehabilitation", "Ultrasound_Machine"]},
    {"id": "H049", "name": "Kamakshi Memorial Hospital, Pallikaranai", "lat": 12.9369, "lon": 80.2120, "capacity": {"icu_beds": 35, "general_beds": 220, "ventilators": 15}, "resources": ["Oncology", "Linear_Accelerator", "PET-CT", "CT_Scanner", "Cath_Lab"]},
    {"id": "H050", "name": "Sugam Hospital, Tiruvottiyur", "lat": 13.1539, "lon": 80.3021, "capacity": {"icu_beds": 15, "general_beds": 85, "ventilators": 5}, "resources": ["Emergency_Medicine", "General_Surgery", "Blood_Bank_Refrigerator"]},
    {"id": "H051", "name": "KVT Speciality Hospital, Tondiarpet", "lat": 13.1311, "lon": 80.2885, "capacity": {"icu_beds": 22, "general_beds": 125, "ventilators": 8}, "resources": ["Orthopedics", "Trauma_Surgeon", "Digital_X-Ray", "ICU_Ventilator"]},
    {"id": "H052", "name": "Apollo Women's Hospital, Thousand Lights", "lat": 13.0620, "lon": 80.2525, "capacity": {"icu_beds": 15, "general_beds": 90, "ventilators": 6}, "resources": ["Obstetrics_&_Gynecology", "Neonatal_Incubator", "Maternal-Fetal_Medicine", "Mammography_Machine"]},
    {"id": "H053", "name": "Cloudnine Hospital, T Nagar", "lat": 13.0395, "lon": 80.2330, "capacity": {"icu_beds": 10, "general_beds": 65, "ventilators": 4}, "resources": ["Neonatology", "Paediatric_ICU", "Radiant_Warmer", "Obstetric_Ultrasound"]},
    {"id": "H054", "name": "Motherhood Hospital, Alwarpet", "lat": 13.0315, "lon": 80.2541, "capacity": {"icu_beds": 12, "general_beds": 70, "ventilators": 5}, "resources": ["Gynecologic_Oncology", "Neonatal_Ventilator", "Fetal_Monitor_CTG"]},
    {"id": "H055", "name": "Rainbow Children's Hospital, Guindy", "lat": 13.0118, "lon": 80.2223, "capacity": {"icu_beds": 25, "general_beds": 130, "ventilators": 12}, "resources": ["Pediatrics", "Neonatology", "Paediatric_ICU", "Transport_Incubator", "High-Flow_Nasal_Cannula"]},
    {"id": "H056", "name": "Sree Balaji Medical College Hospital, Chromepet", "lat": 12.9567, "lon": 80.1425, "capacity": {"icu_beds": 60, "general_beds": 450, "ventilators": 25}, "resources": ["Trauma_Surgeon", "CT_Scanner", "MRI", "Medical_Oxygen_Plant", "General_Surgery"]},
    {"id": "H057", "name": "Saveetha Medical College Hospital, Thandalam", "lat": 13.0298, "lon": 80.0526, "capacity": {"icu_beds": 75, "general_beds": 500, "ventilators": 30}, "resources": ["Cath_Lab", "Burn_Unit", "Trauma_Surgeon", "CT_Scanner", "Oxygen_Pipeline_System"]},
    {"id": "H058", "name": "Panimalar Medical College Hospital, Poonamallee", "lat": 13.0489, "lon": 80.0880, "capacity": {"icu_beds": 50, "general_beds": 400, "ventilators": 20}, "resources": ["Emergency_Medicine", "Digital_X-Ray", "Blood_Bank_Refrigerator", "Dialysis_Chair_Bed"]},
    {"id": "H059", "name": "Aravind Eye Hospital, Poonamallee", "lat": 13.0531, "lon": 80.0988, "capacity": {"icu_beds": 5, "general_beds": 100, "ventilators": 2}, "resources": ["Ophthalmology", "Phacoemulsification_Machine", "Ophthalmic_Laser", "Fundus_Camera", "OCT"]},
    {"id": "H060", "name": "Sankara Nethralaya, Nungambakkam", "lat": 13.0645, "lon": 80.2452, "capacity": {"icu_beds": 10, "general_beds": 150, "ventilators": 4}, "resources": ["Ophthalmology", "Operating_Microscope", "Slit_Lamp", "Optical_Biometer"]},
    {"id": "H061", "name": "Rajan Eye Care, T Nagar", "lat": 13.0410, "lon": 80.2315, "capacity": {"icu_beds": 5, "general_beds": 40, "ventilators": 1}, "resources": ["Ophthalmology", "Phacoemulsification_Machine", "Visual_Field_Analyzer"]},
    {"id": "H062", "name": "Madras ENT Research Foundation, R A Puram", "lat": 13.0215, "lon": 80.2598, "capacity": {"icu_beds": 8, "general_beds": 50, "ventilators": 2}, "resources": ["ENT_Endoscope", "Microscopic_Ear_Surgery_System", "Audiometer"]},
    {"id": "H063", "name": "KKR ENT Hospital, Kilpauk", "lat": 13.0815, "lon": 80.2410, "capacity": {"icu_beds": 6, "general_beds": 45, "ventilators": 1}, "resources": ["ENT", "Laryngoscope", "Nasal_Endoscope"]},
    {"id": "H064", "name": "Right Hospitals, Kilpauk", "lat": 13.0800, "lon": 80.2385, "capacity": {"icu_beds": 15, "general_beds": 75, "ventilators": 5}, "resources": ["Plastic_Surgery", "Orthopedics", "C-Arm", "Digital_X-Ray"]},
    {"id": "H065", "name": "Kumaran Hospital, Kilpauk", "lat": 13.0825, "lon": 80.2392, "capacity": {"icu_beds": 20, "general_beds": 100, "ventilators": 8}, "resources": ["Internal_Medicine", "General_Surgery", "ICU_Ventilator"]},
    {"id": "H066", "name": "VS Hospitals, Chetpet", "lat": 13.0760, "lon": 80.2390, "capacity": {"icu_beds": 25, "general_beds": 120, "ventilators": 10}, "resources": ["Oncology", "Hematology", "Chemotherapy_Infusion_Pump", "CT_Scanner"]},
    {"id": "H067", "name": "Padmini Nursing Home, Chetpet", "lat": 13.0745, "lon": 80.2400, "capacity": {"icu_beds": 5, "general_beds": 40, "ventilators": 2}, "resources": ["Obstetrics_&_Gynecology", "Fetal_Monitor_CTG", "Ultrasound_Machine"]},
    {"id": "H068", "name": "Noble Hospital, Purasawalkam", "lat": 13.0885, "lon": 80.2520, "capacity": {"icu_beds": 12, "general_beds": 65, "ventilators": 4}, "resources": ["General_Surgery", "Patient_Monitor", "Digital_X-Ray"]},
    {"id": "H069", "name": "Murugan Hospital, Kilpauk", "lat": 13.0830, "lon": 80.2420, "capacity": {"icu_beds": 10, "general_beds": 55, "ventilators": 3}, "resources": ["Internal_Medicine", "Defibrillator", "Oxygen_Concentrator"]},
    {"id": "H070", "name": "Hycare Super Speciality Hospital, Arumbakkam", "lat": 13.0705, "lon": 80.2105, "capacity": {"icu_beds": 15, "general_beds": 80, "ventilators": 6}, "resources": ["Neurology", "Orthopedics", "Digital_X-Ray"]},
    {"id": "H071", "name": "Prime Indian Hospitals, Arumbakkam", "lat": 13.0720, "lon": 80.2085, "capacity": {"icu_beds": 20, "general_beds": 90, "ventilators": 8}, "resources": ["Trauma_Surgeon", "Emergency_Medicine", "CT_Scanner"]},
    {"id": "H072", "name": "New Hope Medical Center, Kilpauk", "lat": 13.0812, "lon": 80.2370, "capacity": {"icu_beds": 18, "general_beds": 85, "ventilators": 7}, "resources": ["Gastroenterology", "Upper_GI_Endoscope", "Patient_Monitor"]},
    {"id": "H073", "name": "Appasamy Hospitals, Arumbakkam", "lat": 13.0735, "lon": 80.2090, "capacity": {"icu_beds": 15, "general_beds": 75, "ventilators": 5}, "resources": ["Internal_Medicine", "Ophthalmology", "Slit_Lamp"]},
    {"id": "H074", "name": "Faith Multispeciality Hospital, Villivakkam", "lat": 13.1060, "lon": 80.2050, "capacity": {"icu_beds": 12, "general_beds": 65, "ventilators": 4}, "resources": ["General_Surgery", "Orthopedics", "X-Ray_Machine"]},
    {"id": "H075", "name": "Rabindran's Health Care, Ambattur", "lat": 13.1110, "lon": 80.1570, "capacity": {"icu_beds": 18, "general_beds": 80, "ventilators": 6}, "resources": ["Internal_Medicine", "Obstetrics_&_Gynecology", "Fetal_Monitor_CTG"]},
    {"id": "H076", "name": "Sir Ivan Stedeford Hospital, Ambattur", "lat": 13.1095, "lon": 80.1550, "capacity": {"icu_beds": 25, "general_beds": 180, "ventilators": 10}, "resources": ["General_Surgery", "Dialysis_Chair_Bed", "Blood_Bank_Refrigerator"]},
    {"id": "H077", "name": "Chennai Fertility Center, Aminjikarai", "lat": 13.0715, "lon": 80.2240, "capacity": {"icu_beds": 5, "general_beds": 35, "ventilators": 2}, "resources": ["Infertility_IVF_Equipment", "Ultrasound_Machine"]},
    {"id": "H078", "name": "Best Hospital, Kodambakkam", "lat": 13.0480, "lon": 80.2220, "capacity": {"icu_beds": 10, "general_beds": 60, "ventilators": 3}, "resources": ["Internal_Medicine", "Digital_X-Ray", "Defibrillator"]},
    {"id": "H079", "name": "Mohan Hospital, Valasaravakkam", "lat": 13.0390, "lon": 80.1760, "capacity": {"icu_beds": 8, "general_beds": 50, "ventilators": 2}, "resources": ["Family_Medicine", "Ultrasound_Machine"]},
    {"id": "H080", "name": "Qura Hospital, Thiruvanmiyur", "lat": 12.9850, "lon": 80.2580, "capacity": {"icu_beds": 12, "general_beds": 65, "ventilators": 4}, "resources": ["Internal_Medicine", "Digital_X-Ray"]},
    {"id": "H081", "name": "Dr Rai Memorial Cancer Institute, Teynampet", "lat": 13.0410, "lon": 80.2510, "capacity": {"icu_beds": 15, "general_beds": 80, "ventilators": 5}, "resources": ["Oncology", "Radiation_Therapy_Simulator", "Chemotherapy_Infusion_Pump"]},
    {"id": "H082", "name": "Laksha Hospital, Mylapore", "lat": 13.0350, "lon": 80.2660, "capacity": {"icu_beds": 10, "general_beds": 55, "ventilators": 3}, "resources": ["General_Surgery", "Patient_Monitor", "Digital_X-Ray"]},
    {"id": "H083", "name": "National Hospital, Chennai", "lat": 13.0900, "lon": 80.2780, "capacity": {"icu_beds": 20, "general_beds": 100, "ventilators": 8}, "resources": ["Internal_Medicine", "ICU_Ventilator", "Digital_X-Ray"]},
    {"id": "H084", "name": "CSI Rainy Hospital, Royapuram", "lat": 13.1115, "lon": 80.2910, "capacity": {"icu_beds": 25, "general_beds": 180, "ventilators": 10}, "resources": ["General_Surgery", "Obstetrics_&_Gynecology", "Blood_Bank_Refrigerator"]},
    {"id": "H085", "name": "Mufaddal Polyclinic, Royapuram", "lat": 13.1105, "lon": 80.2890, "capacity": {"icu_beds": 5, "general_beds": 30, "ventilators": 1}, "resources": ["Family_Medicine", "X-Ray_Machine"]},
    {"id": "H086", "name": "Suman Hospital, Thiruvottiyur", "lat": 13.1610, "lon": 80.3015, "capacity": {"icu_beds": 12, "general_beds": 60, "ventilators": 4}, "resources": ["Internal_Medicine", "Digital_X-Ray", "Patient_Monitor"]},
    {"id": "H087", "name": "Leela Speciality Hospital, Thiruvottiyur", "lat": 13.1580, "lon": 80.3030, "capacity": {"icu_beds": 15, "general_beds": 75, "ventilators": 5}, "resources": ["Orthopedics", "Trauma_Surgeon", "C-Arm"]},
    {"id": "H088", "name": "Anand Hospital, Manali", "lat": 13.1700, "lon": 80.2620, "capacity": {"icu_beds": 10, "general_beds": 55, "ventilators": 3}, "resources": ["General_Surgery", "X-Ray_Machine"]},
    {"id": "H089", "name": "Sri Kumaran Hospital, Madhavaram", "lat": 13.1480, "lon": 80.2315, "capacity": {"icu_beds": 15, "general_beds": 80, "ventilators": 5}, "resources": ["Emergency_Medicine", "Trauma_Surgeon", "Digital_X-Ray"]},
    {"id": "H090", "name": "Shree Hospitals, Tondiarpet", "lat": 13.1250, "lon": 80.2820, "capacity": {"icu_beds": 12, "general_beds": 65, "ventilators": 4}, "resources": ["Internal_Medicine", "Defibrillator", "Oxygen_Concentrator"]},
    {"id": "H091", "name": "Jothy Hospital, Tondiarpet", "lat": 13.1280, "lon": 80.2840, "capacity": {"icu_beds": 8, "general_beds": 45, "ventilators": 2}, "resources": ["Obstetrics_&_Gynecology", "Fetal_Monitor_CTG"]},
    {"id": "H092", "name": "Renuka Hospital, Tondiarpet", "lat": 13.1305, "lon": 80.2860, "capacity": {"icu_beds": 10, "general_beds": 50, "ventilators": 3}, "resources": ["General_Surgery", "Ultrasound_Machine"]},
    {"id": "H093", "name": "Mahaveer Hospital, Washermanpet", "lat": 13.1180, "lon": 80.2830, "capacity": {"icu_beds": 18, "general_beds": 90, "ventilators": 6}, "resources": ["Internal_Medicine", "ICU_Ventilator", "Patient_Monitor"]},
    {"id": "H094", "name": "Pavithra Hospitals, Tondiarpet", "lat": 13.1320, "lon": 80.2895, "capacity": {"icu_beds": 15, "general_beds": 75, "ventilators": 5}, "resources": ["Orthopedics", "Digital_X-Ray", "C-Arm"]},
    {"id": "H095", "name": "Muthu Hospital, Perambur", "lat": 13.1065, "lon": 80.2440, "capacity": {"icu_beds": 12, "general_beds": 65, "ventilators": 4}, "resources": ["Family_Medicine", "X-Ray_Machine"]},
    {"id": "H096", "name": "S.G Hospital, Perambur", "lat": 13.1080, "lon": 80.2455, "capacity": {"icu_beds": 10, "general_beds": 55, "ventilators": 3}, "resources": ["General_Surgery", "Digital_X-Ray"]},
    {"id": "H097", "name": "Jupiter Hospital, Perambur", "lat": 13.1105, "lon": 80.2425, "capacity": {"icu_beds": 14, "general_beds": 70, "ventilators": 5}, "resources": ["Internal_Medicine", "Patient_Monitor", "Oxygen_Concentrator"]},
    {"id": "H098", "name": "Narayana Hospital, Vyasarpadi", "lat": 13.1210, "lon": 80.2530, "capacity": {"icu_beds": 20, "general_beds": 110, "ventilators": 8}, "resources": ["Emergency_Medicine", "Trauma_Surgeon", "CT_Scanner", "ICU_Ventilator"]},
    {"id": "H099", "name": "Ganga Hospital, Ambattur", "lat": 13.1075, "lon": 80.1585, "capacity": {"icu_beds": 18, "general_beds": 95, "ventilators": 6}, "resources": ["Orthopedics", "Trauma_Surgeon", "C-Arm", "Joint_Replacement_Surgical_Instruments"]},
    {"id": "H100", "name": "Institute of Child Health (ICH), Egmore", "lat": 13.0760, "lon": 80.2580, "capacity": {"icu_beds": 60, "general_beds": 350, "ventilators": 25}, "resources": ["Pediatrics", "Neonatology", "Paediatric_ICU", "Neonatal_Ventilator", "Radiant_Warmer", "Transport_Incubator", "Blood_Bank_Refrigerator"]}
]

# ==========================================
# Phase 3: RUN THE ADDITION
# ==========================================
if __name__ == "__main__":
    print(f"\n🚀 AegisLink Database Expansion Tool (100 Explicit Hospitals) starting...")
    
    if MONGO_URI == "paste_your_mongo_uri_here":
        print("🛑 WAIT! Update MONGO_URI at the top of the file first.")
        sys.exit(1)
    
    collection = get_hospital_collection()
    
    try:
        # Clear out old entries to cleanly insert the full 100 records
        collection.delete_many({})
        print("🧹 Cleaned existing database entries.")
        
        print(f"\n🛰️ Pushing all {len(NEW_HOSPITALS)} fully parameterized Chennai hospitals to MongoDB Atlas...")
        result = collection.insert_many(NEW_HOSPITALS)
        print(f"\n✅ SUCCESS! Added {len(result.inserted_ids)} massive hospitals to your database.")
        print("🎉 Ready for your showcase! Refresh your Vercel web app.")
        
    except Exception as e:
        print(f"\n🛑 CRITICAL ERROR: {e}")
        sys.exit(1)
