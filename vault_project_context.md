# 🛠️ Secure Document Vault — Project Context

**Challenge:** [Nuit de l’Info 500 — Coffre‑Fort Documentaire Sûr et Intelligent](https://www.nuitdelinfo.com/inscription/defis/500)  

**Timeframe:** 3 hours initial dev sprint  

---

## 1️⃣ Project Goal

Build a **secure, dockerized document vault** with:

- Document storage + search (using Mayan EDMS)
- Role-based access (Admin / User)
- Optional AI features (OCR, summarization)
- Optional SSO / OAuth login  
- Dockerized environment with backend + frontend + DB  

Deliverables:

1. Functional dockerized app  
2. README + instructions  
3. Optional demo video  

---

## 2️⃣ Tech Stack

| Layer | Technology | Notes |
|-------|------------|-------|
| Backend | FastAPI (Python 3.11+) | Async, auto-validation, REST API, connects to Mayan, supports AI/SSO |
| Frontend | Next.js (React + TypeScript) | File upload UI, search UI, admin dashboard |
| Document Engine | Mayan EDMS | Secure document storage, OCR, search API |
| Database | PostgreSQL | Used by Mayan |
| Containerization | Docker + Docker Compose | Networked containers, persistent volumes |

---

## 3️⃣ Technical Skeleton

**Docker Compose Services:**

1. **PostgreSQL**  
   - `POSTGRES_DB=mayandb`  
   - `POSTGRES_USER=mayan`  
   - `POSTGRES_PASSWORD=mayanpass`

2. **Mayan EDMS**  
   - Image: `mayanedms/mayanedms:latest`  
   - Connects to PostgreSQL  
   - Exposed on `localhost:8000`  

3. **Backend (FastAPI)**  
   - Empty skeleton to start  
   - Exposed on `localhost:5000`  
   - Connects to Mayan EDMS API  
   - Ready for role-based auth + AI + SSO  

4. **Frontend (Next.js)**  
   - Exposed on `localhost:3000`  
   - Connects to FastAPI via REST API  

**Volumes:**  
- `postgres_data` → PostgreSQL persistence  
- `mayan_data` → Mayan persistence  

---

## 4️⃣ Next Development Steps

1. **Hour 1–2:**  
   - Launch docker-compose skeleton  
   - Verify Mayan EDMS + PostgreSQL + backend containers  
   - Test API reachability (FastAPI `/` endpoint)  

2. **Hour 2–3:**  
   - Add role-based auth (JWT / RBAC)  
   - Connect backend → Mayan API  
   - Minimal frontend: upload, search, list documents  
   - Test file upload + search + access restrictions  

3. **Optional / Bonus:**  
   - AI features (summaries, embeddings, OCR enhancements)  
   - SSO / OAuth login  
   - Full Next.js UI polishing  

---

## 5️⃣ Key References / Tips

- Mayan API docs: https://docs.mayan-edms.com/  
- FastAPI docs: https://fastapi.tiangolo.com/  
- Next.js docs: https://nextjs.org/docs  
- Docker & Compose docs: https://docs.docker.com/compose/  

**CORS Tip:** FastAPI must allow requests from `localhost:3000` for frontend.  

---

## 6️⃣ Minimal FastAPI Skeleton Example

```python
from fastapi import FastAPI

app = FastAPI(title="Vault Backend")

@app.get("/")
def home():
    return {"message": "Backend is up!"}
```

- Expose port 5000  
- Async-ready for document API calls  

---

## 7️⃣ Docker Compose Skeleton (Summary)

```yaml
services:
  postgres: ...
  mayan: ...
  backend: ...
  frontend: ...
```

- Ensure network `vaultnet`  
- Persistent volumes for DB + Mayan  

---

This file is portable, minimal, and anti-gravity friendly: you can drop it in your repo as `PROJECT_CONTEXT.md` and continue dev seamlessly.

