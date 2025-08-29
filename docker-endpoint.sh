#!/usr/bin/env bash
set -euo pipefail

echo "==> Bootstrapping container..."

# Ambil URL dari env (urutan prioritas)
DB_URL="${DATABASE_URL:-${DB_URL:-${SQLALCHEMY_DATABASE_URI:-${POSTGRES_URL:-}}}}"
if [ -z "${DB_URL}" ]; then
  echo "ERROR: DATABASE_URL (atau DB_URL/SQLALCHEMY_DATABASE_URI/POSTGRES_URL) tidak ditemukan di environment." >&2
  exit 1
fi

# Ganti prefix agar psycopg2 paham
DB_URL_PG="$(echo "$DB_URL" | sed 's#postgresql+psycopg2#postgresql#')"
export DB_URL_PG

echo "==> Using DATABASE_URL: $DATABASE_URL"
echo "==> Normalized for psycopg2: $DB_URL_PG"

echo "==> Waiting for Postgres..."
python - <<'PYCODE'
import os, sys, time, psycopg2, urllib.parse

url = os.environ.get("DB_URL_PG") or ""
print(f"Parsed DSN: {url}")

db_name = urllib.parse.urlparse(url).path.lstrip("/")
print(f"Target database: {db_name}")

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

RUN_ALEMBIC="${RUN_ALEMBIC:-1}"  
ALEMBIC_STAMP_IF_MISSING="${ALEMBIC_STAMP_IF_MISSING:-0}"  
ALEMBIC_AUTO_GENERATE="${ALEMBIC_AUTO_GENERATE:-0}"  

MIGR_DIR="alembic"
[ ! -d "$MIGR_DIR" ] && [ -d "migrations" ] && MIGR_DIR="migrations"

if [ "$RUN_ALEMBIC" != "0" ] && [ -f "alembic.ini" ] && [ -d "$MIGR_DIR" ]; then
  echo "==> Running Alembic (dir: $MIGR_DIR)"
  VERS_DIR="$MIGR_DIR/versions"

  if [ -d "$VERS_DIR" ] && [ -z "$(ls -A "$VERS_DIR" 2>/dev/null || true)" ]; then
    echo "No migrations found. Autogenerating initial revision (dev only)..."
    alembic revision --autogenerate -m "auto-initial-$(date +%Y%m%d%H%M%S)" || true
  fi

  if [ "$ALEMBIC_AUTO_GENERATE" = "1" ]; then
    echo "ALEMBIC_AUTO_GENERATE=1 -> creating autogen revision..."
    alembic revision --autogenerate -m "auto-$(date +%Y%m%d%H%M%S)" || true
  fi

  set +e
  UPG_OUT="$(alembic upgrade head 2>&1)"
  UPG_CODE="$?"
  set -e
  echo "$UPG_OUT"

  if [ "$UPG_CODE" -ne 0 ]; then
    if echo "$UPG_OUT" | grep -q "Can't locate revision identified by"; then
      MISSING_ID="$(printf "%s" "$UPG_OUT" | sed -n "s/.*identified by '\([0-9a-f]\+\)'.*/\1/p" | head -n1)"
      echo "==> Detected missing revision in DB: ${MISSING_ID:-<unknown>}"

      if [ "$ALEMBIC_STAMP_IF_MISSING" = "1" ]; then
        echo "==> ALEMBIC_STAMP_IF_MISSING=1 -> Stamping DB to current head (ASSUMES schema matches code)"
        alembic stamp head
        echo "==> Stamp complete. Continuing startup."
      else
        echo "ERROR: Alembic upgrade failed karena revision hilang di repo."
        echo "Tips:"
        echo "  - Set RUN_ALEMBIC=0 untuk skip Alembic sama sekali (recommended kalau kamu ignore migrations)."
        echo "  - Atau set ALEMBIC_STAMP_IF_MISSING=1 untuk auto 'alembic stamp head' (gunakan dengan paham risikonya)."
        exit 1
      fi
    else
      echo "ERROR: Alembic failed (non-missing-revision). Lihat output di atas."
      exit "$UPG_CODE"
    fi
  fi
else
  echo "==> Alembic skipped (RUN_ALEMBIC=0 atau alembic.ini/folder tidak ada)."
fi

echo "==> Starting app: $*"
exec "$@"
