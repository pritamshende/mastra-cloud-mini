from fastapi import FastAPI
import os
from dotenv import load_dotenv

load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY", "Not Set")

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Mastra AI Placeholder Running", "OPENAI_API_KEY": openai_key}