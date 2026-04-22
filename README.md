#  HNG14 STAGE 2 - DEVOPS: CONTAINERIZED MICROSERVICES

##  Overview

This project is a containerized **Job Processing System** built as part of the HNG DevOps Stage 2 task.

The system consists of:

- **Frontend (Node.js):** Allows users to submit and track jobs  
- **API (FastAPI):** Handles job creation and status retrieval  
- **Worker (Python):** Processes jobs from a queue  
- **Redis:** Acts as a message broker between API and worker

It demonstrates a full **end-to-end DevOps workflow** including:
- CI/CD automation
- Container orchestration
- Service communication
- Security scanning
- Integration testing

---

##  Architecture

```
Frontend → API → Redis Queue → Worker → Redis → API → Frontend
```

All services communicate over a Docker internal network using Docker Compose.

---

##  Tech Stack

- Python 3.12
- FastAPI
- Redis 7
- Node.js 18
- Docker & Docker Compose
- GitHub Actions
- Trivy (Security scanning)
- Pytest (Testing)

---

##  Project Structure

```
hng14-stage2-devops/
│
├── api/           # FastAPI backend
├── worker/        # Background job processor
├── frontend/      # Node.js UI
├── docker-compose.yml
├── .github/workflows/   # CI/CD pipeline
├── FIXES.md
└── README.md
```

---

## Prerequisites

- Docker
- Docker Compose

---

## Environment Variables

Create a `.env` file using the example below:

```
REDIS_URL=redis://redis:6379
API_URL=http://api:8000
PORT=3000
```

---

## How to Run the Application

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd hng14-stage2-devops
```

### 2. Start all services

```bash
docker compose up --build
```

### 3. Stop services

```bash
docker compose down
```

---

## Services

| Service | URL | Description |
|---------|-----|-------------|
| Frontend | http://localhost:3000 | Used to submit jobs and track status |
| API | http://localhost:8000 | Backend API |
| Swagger Docs | http://localhost:8000/docs | API documentation |
| Redis | Internal only | Not exposed to host |

---

## API Endpoints

### Create Job
```
POST /jobs
```

Response:
```json
{
  "job_id": "uuid"
}
```

### Get Job Status
```
GET /jobs/{job_id}
```

Response:
```json
{
  "job_id": "uuid",
  "status": "queued | processing | done"
}
```

### Health Check
```
GET /health
```

Response:
```json
{
  "status": "ok"
}
```

---

##  Status Flow

```
queued → processing → done
```

---

## Running Tests

```bash
cd api
python -m pytest -v
```

---

## CI/CD Pipeline

The GitHub Actions pipeline includes the following stages:

| Stage | Tools |
|-------|-------|
| Linting | flake8 (Python), eslint (JavaScript), hadolint (Docker) |
| Testing | pytest with coverage, Redis integration service |
| Build | Docker image build for all services |
| Security Scan | Trivy vulnerability scanning |
| Integration Test | Full job lifecycle test (API → Redis → Worker) |
| Deploy | Rolling update simulation using Docker Compose |

---

##  Security Improvements

- Removed hardcoded credentials
- Used environment variables (`REDIS_URL`, `API_URL`)
- Added non-root users in containers
- Internal Docker network for Redis
- Vulnerability scanning with Trivy

---

## Key Features

- Multi-service architecture using Docker
- Non-root containers for security
- Health checks for all services
- Environment-based configuration
- Full CI/CD pipeline
- Automated testing with pytest

---

##  Features Completed

- [x] Job creation API
- [x] Background worker processing
- [x] Redis queue system
- [x] Frontend dashboard
- [x] Dockerized microservices
- [x] Full CI/CD pipeline
- [x] Security scanning
- [x] Integration testing

---

## Notes

- `.env` is excluded from the repository for security reasons
- `.env.example` is provided as a template
- Redis is only accessible within the Docker network
- Pipeline runs automatically on push to master


---

## Additional Documentation

See `FIXES.md` for a full breakdown of issues and resolutions.
```