from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import os
import sys

# Tambahkan untuk baca .env
from decouple import config

# Inject app path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

# Import model
from app.models import user  # pastikan semua model diimport
from app.models.user import Base  # base declarative

# --- Alembic Config ---
config_ini = context.config

# Logging config
if config_ini.config_file_name is not None:
    fileConfig(config_ini.config_file_name)

# Inject DATABASE_URL dari .env
database_url = config("DATABASE_URL")  # ambil dari .env
config_ini.set_main_option("sqlalchemy.url", database_url)

# --- Metadata for 'autogenerate' support ---
target_metadata = Base.metadata

# --- Offline migration ---
def run_migrations_offline() -> None:
    context.configure(
        url=database_url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

# --- Online migration ---
def run_migrations_online() -> None:
    connectable = engine_from_config(
        config_ini.get_section(config_ini.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )
        with context.begin_transaction():
            context.run_migrations()

# Run migration
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
