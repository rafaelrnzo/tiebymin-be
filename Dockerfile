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
    pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir alembic psycopg2-binary pydantic[email]

# Copy project (main.py, alembic.ini, alembic/ dsb)
COPY . .

# Entrypoint: wait DB + alembic migrate (ENV di-inject oleh server)
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
