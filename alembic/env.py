import os
import sys
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from dotenv import load_dotenv

# Tambahkan root project ke sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import settings & Base
from app.core.config import settings
from app.db.base import Base

# Load .env (kalau belum terload)
load_dotenv()

# Alembic Config object
config = context.config

# Konfigurasi logging
fileConfig(config.config_file_name)

# Target metadata (untuk auto generate migration)
target_metadata = Base.metadata

# Fungsi ambil URL sync database
def get_url():
    return settings.SYNC_DATABASE_URL

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = get_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        # Ambil config alembic dan timpa url
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool,
        url=get_url(),
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True  # opsional, untuk deteksi perubahan tipe kolom
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
