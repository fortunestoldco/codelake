# Dockerfile
FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Install the application
RUN pip install -e .

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV USER_AGENT="codelake/0.1.0 (https://github.com/yourusername/codelake)"

# Expose API port
EXPOSE 8000

# Command to run the service
CMD ["python", "-m", "codelake.main", "--api"]
