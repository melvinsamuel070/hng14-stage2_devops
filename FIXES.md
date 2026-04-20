
---

# 📄 FIXES.md (FINAL VERSION)

```markdown
# FIXES DOCUMENTATION - STAGE 2 DEVOPS

This document outlines all issues found in the provided application and how they were resolved.

---

## 1. Hardcoded Redis Connection in API

**File:** api/main.py  
**Issue:** Redis connection was hardcoded to `localhost`, which fails inside Docker containers.  
**Fix:** Replaced with environment variable `REDIS_URL` using `os.getenv()`.

---

## 2. Missing Health Check Endpoint

**File:** api/main.py  
**Issue:** No `/health` endpoint existed, causing Docker HEALTHCHECK to fail.  
**Fix:** Added `/health` endpoint returning `{ "status": "ok" }`.

---

## 3. Worker Redis Connection Failure

**File:** worker/worker.py  
**Issue:** Worker attempted to connect to Redis via `localhost`, failing in containerized environment.  
**Fix:** Updated worker to use `REDIS_URL` environment variable.

---

## 4. Frontend API URL Misconfiguration

**File:** frontend/app.js  
**Issue:** API URL was hardcoded to `localhost`, which does not work in Docker Compose networking.  
**Fix:** Replaced with environment variable `API_URL`.

---

## 5. Frontend Undefined Job ID

**File:** frontend/app.js  
**Issue:** UI displayed "Submitted: undefined" due to incorrect response handling.  
**Fix:** Updated logic to correctly read `job_id` from API response.

---

## 6. Docker Networking Issues

**Issue:** Services could not communicate due to use of `localhost`.  
**Fix:** Introduced Docker Compose networking and used service names (`api`, `redis`) as hosts.

---

## 7. Missing Non-Root Users in Containers

**Files:** All Dockerfiles  
**Issue:** Containers were running as root user, which is a security risk.  
**Fix:** Created and used a non-root user (`appuser`) in all containers.

---

## 8. Missing Health Checks in Containers

**Files:** Dockerfiles  
**Issue:** No health checks defined for services.  
**Fix:** Added HEALTHCHECK instructions to ensure service availability.

---

## 9. Missing Unit Tests

**Issue:** No test coverage for API endpoints.  
**Fix:** Added pytest tests for:
- Job creation
- Job retrieval
- Health endpoint

---

## 10. Pytest Environment Misconfiguration

**Issue:** Tests initially failed due to system pytest being used instead of virtual environment.  
**Fix:** Installed pytest inside venv and used `python -m pytest`.

---

## 11. Missing CI/CD Pipeline

**Issue:** No automation for linting, testing, or deployment.  
**Fix:** Implemented GitHub Actions pipeline with stages:
- lint
- test
- build
- security scan
- integration test
- deploy

---

## 12. Redis Exposure Risk

**Issue:** Redis was initially exposed to host machine.  
**Fix:** Restricted Redis to internal Docker network only.

---

# END OF FIXES