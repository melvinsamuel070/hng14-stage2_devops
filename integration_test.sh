#!/usr/bin/env bash
set -e

echo "Running integration tests..."

curl -f http://localhost:8000/health

curl -X POST http://localhost:8000/jobs

curl http://localhost:8000/jobs/invalid-id

echo "All tests passed"