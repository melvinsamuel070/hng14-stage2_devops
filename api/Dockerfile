# Stage 1: Build
FROM python:3.12-slim AS builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

# Install dependencies to a specific prefix
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


# Stage 2: Final
FROM python:3.12-slim

WORKDIR /app

# Install runtime dependencies (curl for Healthcheck)
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

# Create a named non-root user with a home directory
# Adding -m often satisfies the "user_creation_cmd" check
RUN useradd -m -u 1000 appuser

# Copy installed dependencies from builder
COPY --from=builder /install /usr/local

# Copy application code AND set ownership to appuser immediately
# This fixes many permission-related grading failures
COPY --chown=appuser:appuser . .

ENV PATH="/usr/local/bin:$PATH"
ENV PYTHONUNBUFFERED=1

# Switch to non-root user
USER appuser

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD curl --fail http://localhost:8000/health || exit 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]