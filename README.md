# 🛡️ Secure Document Vault

A secure, dockerized document management system with role-based access control, AI-powered analysis, and seamless integration with Mayan EDMS.

**Challenge:** [Nuit de l'Info 500 — Coffre-Fort Documentaire Sûr et Intelligent](https://www.nuitdelinfo.com/inscription/defis/500)

## 🏗️ Architecture

```
┌─────────────┐     ┌─────────────┐     ┌──────────────┐
│   Next.js   │────▶│   FastAPI   │────▶│  Mayan EDMS  │
│  Frontend   │     │   Backend   │     │  + OCR/AI    │
└─────────────┘     └─────────────┘     └──────────────┘
                           │
                           ▼
                    ┌──────────────┐
                    │  PostgreSQL  │
                    └──────────────┘
```

## ✨ Features

- 🔐 **Secure Document Storage** via Mayan EDMS
- 🔍 **OCR & Full-Text Search**
- 🤖 **AI-Powered Analysis** (Local LLM)
- 👥 **Role-Based Access Control** (Admin/User)
- 🐳 **Fully Dockerized** - One command deployment
- 🔑 **SSO Ready** (Optional)

## 🚀 Quick Start

### Prerequisites

- Docker Desktop (with at least 4GB RAM allocated)
- Docker Compose

### Setup

1. **Clone and configure:**
   ```bash
   git clone <your-repo>
   cd OCR
   cp .env.example .env
   # Edit .env with your credentials
   ```

2. **Start the application:**
   ```bash
   docker-compose up --build
   ```

3. **Access services:**
   - **Frontend:** http://localhost:3000
   - **Backend API:** http://localhost:5000
   - **API Docs:** http://localhost:5000/api/v1/docs
   - **Mayan EDMS:** http://localhost:8000

## 📁 Project Structure

```
OCR/
├── backend/              # FastAPI backend
│   ├── app/
│   │   ├── api/v1/      # API routes
│   │   ├── core/        # Config & settings
│   │   ├── db/          # Database setup
│   │   ├── models/      # SQLAlchemy models
│   │   ├── schemas/     # Pydantic schemas
│   │   ├── services/    # Business logic
│   │   └── main.py      # App entry point
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/            # Next.js frontend
│   ├── app/
│   └── Dockerfile
├── docker-compose.yml   # Service orchestration
├── .env.example         # Environment template
└── README.md
```

## 🔧 Development

### Backend (FastAPI)

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend (Next.js)

```bash
cd frontend
npm install
npm run dev
```

## 🧪 API Documentation

Once running, visit:
- **Swagger UI:** http://localhost:5000/api/v1/docs
- **ReDoc:** http://localhost:5000/api/v1/redoc

## 🔐 Environment Variables

Key variables in `.env`:

```env
# Database
POSTGRES_USER=mayan
POSTGRES_PASSWORD=your-password
POSTGRES_DB=mayandb

# Redis
REDIS_HOST=redis
REDIS_PORT=6379

# JWT
SECRET_KEY=your-secret-key
```

## 📝 License

This project was created for the Nuit de l'Info 2024 Challenge.

## 👥 Team

[TEAM SIN_SIRO]
