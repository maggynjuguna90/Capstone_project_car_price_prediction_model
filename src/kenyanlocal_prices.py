# services/kenya_prices.py

import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://postgres:maggy123@localhost:5432/japancars"
)

def get_kenya_price(Make, Model, Year):

    query = f"""
    SELECT Price
    FROM kenya_market_prices
    WHERE Make = '{Make}'
      AND Model = '{Model}'
      AND Year = {Year}
    LIMIT 1
    """

    df = pd.read_sql(query, engine)

    if df.empty:
        return None

    return float(df.iloc[0]["Price"])