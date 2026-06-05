from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "project": "AI Cloud Cost Detective",
        "status": "Running"
    }

@app.get("/health")
def health():
    return {
        "health": "OK"
    }

@app.get("/scan-resources")
def scan_resources():
    return {
        "resources": [
            {
                "name": "vm-prod-01",
                "type": "Virtual Machine",
                "status": "Over-Provisioned",
                "estimated_savings": "$120/month"
            },
            {
                "name": "storage-prod",
                "type": "Storage Account",
                "status": "Unused Logs",
                "estimated_savings": "$35/month"
            }
        ]
    }