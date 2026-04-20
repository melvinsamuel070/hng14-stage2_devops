# hng14-stage2-devops
# HNG14 STAGE 2 - DEVOPS: CONTAINERIZED MICROSERVICES

## Overview

This project is a containerized job processing system built as part of the HNG DevOps Stage 2 task.

The system consists of:

- **Frontend (Node.js):** Allows users to submit and track jobs  
- **API (FastAPI):** Handles job creation and status retrieval  
- **Worker (Python):** Processes jobs from a queue  
- **Redis:** Acts as a message broker between API and worker  

---

## Architecture

Frontend → API → Redis Queue → Worker → Redis → API → Frontend

All services communicate over a Docker internal network using Docker Compose.

---

## Prerequisites

- Docker
- Docker Compose

---

## Environment Variables

Create a `.env` file using the example below:

REDIS_URL=redis://redis:6379
API_URL=http://api:8000

PORT=3000


## How to Run the Application

### 1. Clone the repository

```
git clone <your-repo-url>
cd hng14-stage2-devops

### Start all services
docker compose up --build
### Stop services
docker compose down
```
## This are the Services
Frontend
URL: http://localhost:3000
Used to submit jobs and track status
API
URL: http://localhost:8000
Swagger Docs: http://localhost:8000/docs
Redis
Internal only (not exposed to host)
API Endpoints
Create Job
POST /jobs

Response:

{
  "job_id": "uuid"
}
Get Job Status
GET /jobs/{job_id}

Response:

{
  "job_id": "uuid",
  "status": "queued | processing | done"
}
Health Check
GET /health

Response:

{
  "status": "ok"
}

## Running Tests

cd api
python -m pytest -v
CI/CD Pipeline


## The project uses GitHub Actions with the following stages:

Lint (flake8, eslint, hadolint)
Test (pytest with coverage)
Build (Docker images)
Security Scan (Trivy)
Integration Test (full stack validation)
Deploy (rolling update simulation)
Key Features
Multi-service architecture using Docker
Non-root containers for security
Health checks for all services
Environment-based configuration
Full CI/CD pipeline
Automated testing with pytest
Notes
.env is excluded from the repository for security reasons
.env.example is provided as a template
Redis is only accessible within the Docker network
