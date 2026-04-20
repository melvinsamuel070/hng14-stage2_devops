FROM python:3.12-slim

WORKDIR /app

# Create non-root user
RUN useradd -m appuser

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

USER appuser

ENV PYTHONUNBUFFERED=1

HEALTHCHECK CMD pgrep -f worker.py || exit 1

CMD ["python", "worker.py"]