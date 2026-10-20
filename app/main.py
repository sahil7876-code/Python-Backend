from fastapi import FastAPI

app = FastAPI(title="Student API")

@app.get("/welcome")
def home():
    return {
        "message": "Welcome to Student API"
    }

@app.get("/health")
def home():
    return {
        "message" : "Welcome to the health"
    }

