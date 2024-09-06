# Use Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy the Python script
COPY redis.py .

# Install dependencies
RUN pip install redis

# Command to run the Python script
CMD ["python", "redis.py"]
