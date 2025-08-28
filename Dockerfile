# Use the full image to avoid mediapipe issues
FROM python:3.10

# Python runtime flags
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# System dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    ffmpeg \
    libsm6 \
    libxext6 \
    libgl1 \
    libglib2.0-0 \
  && rm -rf /var/lib/apt/lists/*

# Workdir
WORKDIR /app

# Install deps (cache-friendly)
COPY requirements.txt ./requirements.txt
RUN python -m pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install pydantic[email]

# Copy the entire project (this brings in main.py at /app/main.py)
COPY . .

# Do NOT copy .env — env comes from the server/orchestrator
EXPOSE 8000

# Start app (main.py is at project root)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
