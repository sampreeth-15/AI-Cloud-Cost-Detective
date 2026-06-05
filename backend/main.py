from fastapi import FastAPI

app = FastAPI()

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