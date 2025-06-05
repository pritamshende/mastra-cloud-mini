
# 🚀 Mastra Cloud Mini – DevOps Assessment

This project simulates a self-service deployment platform for the Mastra AI app. It allows users to deploy a custom instance by submitting their OpenAI API key through a web interface.

---

## 👤 Candidate Information

**Name**: Pritam Shende  
**Position**: DevOps Engineer (Assessment Submission)

---

## 📌 Objective

Build a mini cloud platform that simulates the deployment of the Mastra AI app, allowing end-users to deploy their own hosted and configured app instance.

---

## ✅ What This Project Includes

- ✅ FastAPI-based backend that mimics Mastra deployment behavior.
- ✅ HTML + JavaScript frontend to accept API key input from users.
- ✅ Docker containerization with support for `.env` configuration.
- ✅ Hosting using Render.com for real-time testing and access.

---

## 📦 Project Structure

```
mastra-cloud-mini/
│
├── Dockerfile                 # Container instructions
├── main.py                   # FastAPI app with UI and endpoint
├── requirements.txt          # Python dependencies
├── .env.example              # Example environment file
└── static/
    └── index.html            # UI form for API key input
```

---

## 🧾 Missing from Original Mastra Repo

The original [Mastra GitHub repo](https://github.com/mastra-ai/mastra) did **not include any `.py` files**, making local deployment impossible. Therefore:

- 🔧 A **custom FastAPI app** was created as a placeholder.
- 🧪 Functionality was simulated using environment variables and dummy endpoints.

---

## 🛠️ How I Built This (Step-by-Step)

### Step 1: Clone the Mastra Repo (Initial Attempt)
```bash
git clone https://github.com/mastra-ai/mastra.git
```
**Result**: `.py` files were missing. No clear app entry point.

---

### Step 2: Create Custom App

Created the following files manually:

**main.py**
```python
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import os

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def root():
    with open("static/index.html", "r") as f:
        return f.read()

class DeployRequest(BaseModel):
    api_key: str

@app.post("/deploy")
def deploy_instance(req: DeployRequest):
    return {
        "message": f"✅ Mastra AI instance deployed with API key: {req.api_key}"
    }
```

**static/index.html**
```html
<form id="deployForm">...</form>
<script>...</script>
```

**requirements.txt**
```
fastapi
uvicorn
python-dotenv
```

**.env.example**
```
OPENAI_API_KEY=apikey
```

---

### Step 3: Create Dockerfile

```Dockerfile
FROM python:3.10-slim

WORKDIR /app
COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 7860

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]
```

---

### Step 4: Build and Run Locally

```bash
docker build -t mastra-app .
docker run -p 7860:7860 --env-file .env mastra-app
```

Access app: [http://localhost:7860](http://localhost:7860)

---

### Step 5: Push to GitHub

```bash
git init
git remote add origin https://github.com/pritamshende/mastra-cloud-mini.git
git add .
git commit -m "Initial commit"
git push -u origin main
```

---

### Step 6: Deploy to Render

1. Sign in at [https://render.com](https://render.com)
2. New > Web Service > From GitHub
3. Select repo and configure:
   - **Start Command**:
     ```bash
     uvicorn main:app --host 0.0.0.0 --port 7860
     ```
   - Add `OPENAI_API_KEY` as environment variable
4. Click “Deploy”

Demo URL generated automatically.

---

## 🔚 Final Result

- 🟢 Deployed app simulates Mastra AI cloud deployment.
- 🧪 Accepts real-time API keys.
- 🌐 Fully containerized and live-hosted.

---

## 🗂 GitHub Repository

🔗 [https://github.com/pritamshende/mastra-cloud-mini](https://github.com/pritamshende/mastra-cloud-mini)

---

## 🌐 Live Demo

🔗 [https://mastra-cloud-mini.onrender.com](https://mastra-cloud-mini.onrender.com)

---

### ✅ Submission Ready!

