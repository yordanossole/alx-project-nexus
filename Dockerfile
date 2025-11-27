FROM python:3.12-slim-bookworm

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    redis-server libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /src

# Copy requirements and install Python dependencies with caching
COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --upgrade pip \
    && pip install --default-timeout=200 -i https://pypi.org/simple -r requirements.txt

# Copy project files
COPY . .

# Expose Django port
EXPOSE 8000

# Start Redis and Django
CMD ["sh", "-c", "redis-server & python manage.py runserver 0.0.0.0:8000"]