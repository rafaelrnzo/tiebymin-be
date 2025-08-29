# Use the full image to avoid mediapipe issues
FROM python:3.10

# Python runtime flags
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# System dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    ffmpeg \
    libsm6 \
    libxext6 \
    libgl1 \
    libglib2.0-0 \
    dos2unix \
  && rm -rf /var/lib/apt/lists/*

# Workdir
WORKDIR /app

COPY requirements.txt ./requirements.txt
RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir alembic psycopg2-binary email-validator

COPY . .

RUN mkdir -p alembic/versions

# COPY --chmod=755 docker-endpoint.sh /usr/local/bin/docker-endpoint.sh
# RUN dos2unix /usr/local/bin/docker-endpoint.sh || true

# ENV RUN_ALEMBIC=0
# ENV ALEMBIC_AUTO_GENERATE=0
# ENV ALEMBIC_STAMP_IF_MISSING=0

EXPOSE 8000

# ENTRYPOINT ["/usr/local/bin/docker-endpoint.sh"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
