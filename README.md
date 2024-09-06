# Python Redis Application

This Python application interacts with a Redis database. It continuously inserts and retrieves data from Redis, using environment variables for Redis configuration, making it suitable for Docker and Kubernetes deployment.

## Features
- Inserts data into Redis at regular intervals.
- Retrieves and displays data from Redis.
- Configurable via environment variables for Redis connection details.

---

## Prerequisites

- Python 3.8+
- Docker
- Kubernetes (optional, for Kubernetes deployment)
- Redis instance (local, in Docker, or external)

---

## Local Development Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo

### 2. Install Dependencies
    
    pip install -r requirements.txt

### 3. Set Environment Variables

Set the Redis connection environment variables:
    export REDIS_HOST=localhost
    export REDIS_PORT=6379
    export REDIS_DB=0

### 4. Run the Application

    python redis.py

### Docker

    docker run -e REDIS_HOST=your_redis_host -e REDIS_PORT=6379 -e REDIS_DB=0 farhanaliali/redis-test
### Kubernetes 

update the dpeloyment file according to your needs 

Apply the Python app deployment:

    kubectl create -f deployment.yaml
