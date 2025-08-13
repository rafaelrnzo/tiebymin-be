# Gunakan full image agar mediapipe tidak error
FROM python:3.10

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    ffmpeg \
    libsm6 \
    libxext6 \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt .

# Install dependencies from requirements
RUN pip install --upgrade pip && \
    pip install --no-cache-dir sqlalchemy python-decouple uvicorn opencv-python mediapipe pydantic[email] passlib[bcrypt] && \
    pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY ./app /app
COPY .env .env

# Expose port
EXPOSE 8000

# Run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

