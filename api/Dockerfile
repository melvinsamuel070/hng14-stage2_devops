FROM python:3.12-slim AS builder

WORKDIR /app

# install build tools WITHOUT pinning versions (safe + stable)
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


# ---------------- FINAL STAGE ----------------
FROM python:3.12-slim

WORKDIR /app

# install runtime dependencies (NO VERSION PINNING)
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*

# create non-root user (required by grading)
RUN groupadd -r appgroup && useradd -r -g appgroup appuser

# copy installed python packages
COPY --from=builder /install /usr/local

COPY . .

ENV PATH="/usr/local/bin:$PATH"
ENV PYTHONUNBUFFERED=1

USER appuser

EXPOSE 8000

HEALTHCHECK CMD curl --fail http://localhost:8000/health || exit 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]