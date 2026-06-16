from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    "postgresql://postgres:maggy123@localhost:5432/japancars"
)

def get_all_cars(limit=20):

    query = f"""
    SELECT *
    FROM japan_cars_list
    LIMIT {limit}
    """

    return pd.read_sql(query, engine)


def search_cars(Make):

    query = f"""
    SELECT *
    FROM japan_cars
    WHERE "Make" ILIKE '%{Make}%'
    LIMIT 100
    """

    return pd.read_sql(query, engine)