# backend/main.py
from fastapi import FastAPI

app = FastAPI(title="GyaanMap Roadmap API")

@app.get("/")
async def root():
    return {"message": "GyaanMap Roadmap API is running"}
