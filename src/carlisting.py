from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import pandas as pd
import os

load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


def get_all_cars(limit=20):
    query = text("""
        SELECT *
        FROM japan_cars_list
        LIMIT :limit
    """)

    return pd.read_sql(query, engine, params={"limit": limit})


def search_cars(make):
    query = text("""
        SELECT *
        FROM japan_cars
        WHERE "Make" ILIKE :make
        LIMIT 100
    """)

    return pd.read_sql(
        query,
        engine,
        params={"make": f"%{make}%"}
    )