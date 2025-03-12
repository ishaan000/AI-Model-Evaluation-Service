from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Model Evaluation Service is Running 🚀"}