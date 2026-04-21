# FROM python:3.12-slim AS builder

# WORKDIR /app

# COPY requirements.txt .
# RUN pip install --no-cache-dir --user -r requirements.txt


# # Stage 2
# FROM python:3.12-slim

# WORKDIR /app

# RUN apt-get update && apt-get install -y --no-install-recommends curl=7.88.1-2 && rm -rf /var/lib/apt/lists/*

# RUN useradd -m appuser

# COPY --from=builder /root/.local /home/appuser/.local
# COPY . .

# ENV PATH=/home/appuser/.local/bin:$PATH

# USER appuser

# EXPOSE 8000

# # FIXED HEALTHCHECK (IMPORTANT)
# HEALTHCHECK CMD curl --fail http://localhost:8000/health || exit 1

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]



FROM python:3.12-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt


# Stage 2
FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends curl=8.6.0-3 && rm -rf /var/lib/apt/lists/*

RUN useradd -m appuser

COPY --from=builder /root/.local /home/appuser/.local
COPY . .

ENV PATH=/home/appuser/.local/bin:$PATH

USER appuser

EXPOSE 8000

# FIXED HEALTHCHECK (IMPORTANT)
HEALTHCHECK CMD curl --fail http://localhost:8000/health || exit 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]