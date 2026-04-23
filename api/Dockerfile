# FROM python:3.12-slim AS builder

# WORKDIR /app

# COPY requirements.txt .
# RUN pip install --no-cache-dir --user -r requirements.txt


# # Stage 2
# FROM python:3.12-slim

# WORKDIR /app

# # hadolint ignore=DL3008
# RUN apt-get update && apt-get install -y --no-install-recommends curl && rm -rf /var/lib/apt/lists/*

# RUN useradd -m appuser

# COPY --from=builder /root/.local /home/appuser/.local
# COPY . .

# ENV PATH=/home/appuser/.local/bin:$PATH

# USER appuser

# EXPOSE 8000

# # FIXED HEALTHCHECK (IMPORTANT)
# HEALTHCHECK CMD curl --fail http://localhost:8000/health || exit 1

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


# -------- BUILD STAGE --------
FROM python:3.12-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt


# -------- FINAL STAGE --------
FROM python:3.12-slim

WORKDIR /app

# hadolint ignore=DL3008
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN groupadd -r appgroup && useradd -r -g appgroup appuser

# Copy dependencies
COPY --from=builder /root/.local /root/.local

# Copy app
COPY . .

# Environment
ENV PATH=/root/.local/bin:$PATH
ENV PYTHONUNBUFFERED=1

# Switch to non-root
USER appuser

EXPOSE 8000

# ✅ FIX: add start-period so FastAPI has time to boot
HEALTHCHECK --interval=10s --timeout=5s --retries=5 --start-period=15s \
CMD curl --fail http://localhost:8000/health || exit 1

# Start app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]