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













FROM python:3.12-slim AS builder

WORKDIR /app

# Disable DL3008 because Debian slim does not guarantee stable version pinning
# hadolint ignore=DL3008
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


FROM python:3.12-slim

WORKDIR /app

# hadolint ignore=DL3008
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*

RUN groupadd -r appgroup && useradd -r -g appgroup appuser

COPY --from=builder /install /usr/local
COPY . .

ENV PATH="/usr/local/bin:$PATH"
ENV PYTHONUNBUFFERED=1

USER appuser

EXPOSE 8000

HEALTHCHECK CMD curl --fail http://localhost:8000/health || exit 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]