# kenya_prices.py

# services/kenya_prices.py

import pandas as pd
from sqlalchemy import text

from db import engine


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

    return float(df.iloc[0]["price"])