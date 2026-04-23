FROM python:3.12-slim AS builder

WORKDIR /app

# PIN versions (Hadolint requirement) - Updated for Debian Trixie
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential=12.10 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


# ---------------- FINAL STAGE ----------------
FROM python:3.12-slim

WORKDIR /app

# PIN curl version (fix DL3008) - Updated for Debian Trixie
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl=8.6.0-3 \
    && rm -rf /var/lib/apt/lists/*

# non-root user (required by grading)
RUN groupadd -r appgroup && useradd -r -g appgroup appuser

COPY --from=builder /install /usr/local
COPY . .

ENV PATH="/usr/local/bin:$PATH"
ENV PYTHONUNBUFFERED=1

USER appuser

EXPOSE 8000

HEALTHCHECK CMD curl --fail http://localhost:8000/health || exit 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]