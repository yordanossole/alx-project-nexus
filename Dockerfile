FROM python:3.10

# Install system dependencies
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory to project root (repo root mounted to /src)
WORKDIR /src

# Copy requirements and install first for caching
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

# Ensure Python can import from the src package directory
ENV PYTHONPATH=/src/src

# Run Django on port 8010 and reference manage.py in the src folder
CMD ["python", "src/manage.py", "runserver", "0.0.0.0:8010"]
