# alembic/env.py
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import os
from dotenv import load_dotenv
from app.models import Base 

# Load environment variables
load_dotenv()

# Interpret the config file for Python logging.
fileConfig(context.config.config_file_name)

# Set the target metadata
target_metadata = Base.metadata

# Database URL from environment
DATABASE_URL = os.getenv("DATABASE_URL")


def run_migrations_online():
    connectable = engine_from_config(
        {"sqlalchemy.url": DATABASE_URL},
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


run_migrations_online()
