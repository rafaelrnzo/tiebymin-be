#!/usr/bin/env bash
set -euo pipefail

echo "==> Bootstrapping container..."

DB_URL="${DATABASE_URL:-${DB_URL:-${SQLALCHEMY_DATABASE_URI:-${POSTGRES_URL:-}}}}"
if [ -z "${DB_URL}" ]; then
  echo "ERROR: DATABASE_URL (atau DB_URL/SQLALCHEMY_DATABASE_URI/POSTGRES_URL) tidak ditemukan di environment." >&2
  exit 1
fi

DB_URL_PG="${DB_URL//postgresql+psycopg2/postgresql}"
export DB_URL_PG

echo "==> Waiting for Postgres: $DB_URL_PG"
python - <<'PYCODE'
import os, sys, time
import psycopg2
url = os.environ.get("DB_URL_PG") or ""
for i in range(60):
    try:
        conn = psycopg2.connect(url)
        conn.close()
        print("Postgres is up!")
        break
    except Exception as e:
        print(f"Waiting for Postgres... ({i+1}/60) {e}")
        time.sleep(1)
else:
    print("ERROR: Postgres is not reachable within timeout.", file=sys.stderr)
    sys.exit(1)
PYCODE

MIGR_DIR="alembic"
[ ! -d "$MIGR_DIR" ] && [ -d "migrations" ] && MIGR_DIR="migrations"

if [ -f "alembic.ini" ] && [ -d "$MIGR_DIR" ]; then
  echo "==> Running Alembic (dir: $MIGR_DIR)"
  VERS_DIR="$MIGR_DIR/versions"
  if [ -d "$VERS_DIR" ] && [ -z "$(ls -A "$VERS_DIR" 2>/dev/null || true)" ]; then
    echo "No migrations found. Autogenerating initial revision..."
    alembic revision --autogenerate -m "auto-initial-$(date +%Y%m%d%H%M%S)" || true
  fi

  if [ "${ALEMBIC_AUTO_GENERATE:-0}" = "1" ]; then
    echo "ALEMBIC_AUTO_GENERATE=1 -> creating autogen revision..."
    alembic revision --autogenerate -m "auto-$(date +%Y%m%d%H%M%S)" || true
  fi

  alembic upgrade head
else
  echo "==> Alembic not configured (alembic.ini atau folder alembic/ tidak ada). Skipping."
fi

echo "==> Starting app: $*"
exec "$@"
