import redis
import time
import os
import signal

REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379")
r = redis.Redis.from_url(REDIS_URL, decode_responses=True)

def process_job(job_id):
    print(f"Processing job {job_id}")
    time.sleep(2)
    r.hset(f"job:{job_id}", "status", "done")
    print(f"Done: {job_id}")

print("Worker started...")

while True:
    job = r.brpop("jobs", timeout=5)
    if job:
        _, job_id = job
        process_job(job_id)