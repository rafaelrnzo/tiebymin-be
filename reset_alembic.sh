cat >/app/reset_and_migrate.sh <<'BASH'
#!/usr/bin/env bash
set -euo pipefail

# ====== KONFIG ======
DB_HOST="${DB_HOST:-minecraft-server_tiebymin-db}"   # ganti kalau host Postgres kamu beda (mis. tiebymin-db)
DB_USER="${DB_USER:-admin}"
DB_PASS="${DB_PASS:-admin.admin}"
DB_NAME="${DB_NAME:-tiebymin_db}"

echo "==> Using Postgres: host=$DB_HOST db=$DB_NAME user=$DB_USER"

# ====== Tools check ======
if ! command -v psql >/dev/null 2>&1; then
  echo "==> Installing postgresql-client..."
  apt-get update && apt-get install -y --no-install-recommends postgresql-client >/dev/null
fi

if ! command -v alembic >/dev/null 2>&1; then
  echo "==> Installing alembic & psycopg2-binary..."
  python -m pip install --no-cache-dir alembic psycopg2-binary >/dev/null
fi

# ====== Test koneksi ======
echo "==> Testing DB connection..."
PGPASSWORD="$DB_PASS" psql -h "$DB_HOST" -U "$DB_USER" -d "$DB_NAME" -c "SELECT current_database(), current_user();" >/dev/null

# ====== Drop schema public (bersihkan semua tabel) ======
echo "==> Dropping and recreating schema public..."
PGPASSWORD="$DB_PASS" psql -h "$DB_HOST" -U "$DB_USER" -d "$DB_NAME" \
  -c "DROP SCHEMA IF EXISTS public CASCADE; CREATE SCHEMA public;"

# ====== Sinkron Alembic dari nol ======
cd /app

# Pastikan folder versions ada
mkdir -p alembic/versions

# (opsional kuat): bersihkan migration lama biar bener2 baseline baru
# Hapus semua .py di versions, tapi JANGAN hapus foldernya
echo "==> Cleaning old migrations (alembic/versions/*.py)..."
find alembic/versions -maxdepth 1 -type f -name "*.py" -print -delete || true

# Samakan DB ke 'base' tanpa menjalankan migration apa pun
echo "==> Alembic stamp base..."
alembic stamp base

# Generate migration awal berdasarkan model saat ini
echo "==> Alembic autogenerate baseline..."
alembic revision --autogenerate -m "baseline $(date +%F)"

# Jalankan migration ke head
echo "==> Alembic upgrade head..."
alembic upgrade head

# ====== Verifikasi ======
echo "==> Verifying tables..."
PGPASSWORD="$DB_PASS" psql -h "$DB_HOST" -U "$DB_USER" -d "$DB_NAME" -c "\dt"
echo "==> Alembic current:"
alembic current

echo "==> DONE. Database fresh + migrated."
BASH

chmod +x /app/reset_and_migrate.sh
