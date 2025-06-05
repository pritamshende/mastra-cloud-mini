from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import os

app = FastAPI()

# Serve the HTML file
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def root():
    with open("static/index.html", "r") as f:
        return f.read()

# Handle form submission
class DeployRequest(BaseModel):
    api_key: str

@app.post("/deploy")
def deploy_instance(req: DeployRequest):
    # For now, just return a confirmation with the key
    return {
        "message": f"✅ Mastra AI instance deployed with API key: {req.api_key}"
    }