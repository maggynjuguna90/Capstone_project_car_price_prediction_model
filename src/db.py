"""Central database configuration.

Single source of truth for the PostgreSQL connection. Every module that
needs the database should `from db import engine` instead of building its
own engine from environment variables.

Configuration is read from environment variables (loaded from .env):

    DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD

Alternatively, set DATABASE_URL to override the assembled connection string.
"""

import os

from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "japancars")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
)

# Shared engine reused across the app.
engine = create_engine(DATABASE_URL)
