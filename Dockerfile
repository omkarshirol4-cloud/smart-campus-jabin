# Dockerfile
# Container image for KLE Society's P.C. Jabin Science College Smart Campus Platform
FROM python:3.13-slim

WORKDIR /app

# Prevent Python from writing .pyc files and enable unbuffered output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose default Flask port
EXPOSE 5000

# Run Flask application
CMD ["python", "app.py"]
