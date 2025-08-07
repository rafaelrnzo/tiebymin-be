FROM python:3.10-slim

ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN python -m venv $VIRTUAL_ENV

COPY . .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install sqlalchemy psycopg2 python-decouple \
    pip install uvicorn

EXPOSE 8000

COPY app /app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
