
# FIXES DOCUMENTATION - STAGE 2 DEVOPS

This document outlines all issues identified in the application and the fixes applied to ensure full containerized CI/CD functionality.

---

## 1. Hardcoded Redis Connection in API

**File:** api/main.py  
**Issue:** Redis was hardcoded to `localhost`, which fails inside Docker containers.  
**Fix:** Replaced with environment variable `REDIS_URL` using `os.getenv()` to support Docker networking.

---

## 2. Missing Health Check Endpoint

**File:** api/main.py  
**Issue:** `/health` endpoint was missing, causing Docker health checks and CI integration tests to fail.  
**Fix:** Added `/health` endpoint returning `{ "status": "ok" }`.

---

## 3. Worker Redis Connection Failure

**File:** worker/worker.py  
**Issue:** Worker was connecting to Redis via `localhost`, which does not work in containerized environments.  
**Fix:** Updated worker to use `REDIS_URL` environment variable pointing to Docker service name `redis`.

---

## 4. Incorrect Queue Name Between API and Worker

**Issue:** API and worker used different Redis queue names (`job` vs `jobs`).  
**Fix:** Standardized queue name to `jobs` across both services.

---

## 5. Job Status Inconsistency

**Issue:** Worker set job status to `completed` while integration tests expected `done`.  
**Fix:** Standardized job status to `done` across worker and API responses.

---

## 6. Frontend API URL Misconfiguration

**File:** frontend/app.js  
**Issue:** API URL was hardcoded to `localhost`, breaking communication in Docker Compose.  
**Fix:** Replaced with `API_URL` environment variable.

---

## 7. Frontend Undefined Job ID

**File:** frontend/app.js  
**Issue:** UI displayed `Submitted: undefined` due to incorrect response parsing.  
**Fix:** Corrected response handling to properly extract `job_id` from API response.

---

## 8. Docker Networking Issues

**Issue:** Services could not communicate due to use of `localhost`.  
**Fix:** Implemented Docker Compose networking and replaced `localhost` with service names (`api`, `redis`, `worker`).

---

## 9. Missing Non-Root Users in Containers

**Files:** Dockerfiles  
**Issue:** Containers ran as root user, posing a security risk.  
**Fix:** Added non-root user (`appuser`) in all Dockerfiles for secure execution.

---

## 10. Missing Container Health Checks

**Files:** Dockerfiles / docker-compose.yml  
**Issue:** No health checks defined for services.  
**Fix:** Added HEALTHCHECK instructions and Docker Compose health conditions.

---

## 11. Missing Unit Tests

**Issue:** No automated API tests were originally included.  
**Fix:** Added pytest tests covering:
- Job creation
- Job retrieval
- Health endpoint validation

---

## 12. Pytest Environment Misconfiguration

**Issue:** System pytest was used instead of virtual environment, causing missing module errors.  
**Fix:** Installed dependencies inside virtual environment and ran tests using `python -m pytest`.

---

## 13. CI/CD Pipeline Not Implemented Initially

**Issue:** No automation for linting, testing, building, or deployment.  
**Fix:** Implemented GitHub Actions CI/CD pipeline with stages:
- Linting (Python, JS, Docker)
- Unit Testing
- Docker Image Build
- Security Scan (Trivy)
- Integration Testing
- Deployment Simulation

---

## 14. Redis Exposure Risk

**Issue:** Redis was initially exposed outside Docker network.  
**Fix:** Restricted Redis to internal Docker Compose network only.

---

# END OF FIXES