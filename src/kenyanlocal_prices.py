# kenya_prices.py

# services/kenya_prices.py

import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


def get_kenya_price(make, model, year):
    query = text("""
        SELECT Price
        FROM kenya_market_prices
        WHERE UPPER(Make) = UPPER(:make)
          AND UPPER(Model) = UPPER(:model)
          AND Year = :year
        LIMIT 1
    """)

    df = pd.read_sql(
        query,
        engine,
        params={
            "make": make,
            "model": model,
            "year": year
        }
    )

    if df.empty:
        return None

    return float(df.iloc[0]["Price"])