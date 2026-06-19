from sqlalchemy import text
import pandas as pd

from db import engine


def get_all_cars(limit=20):
    query = text("""
        SELECT *
        FROM japan_cars_list
        LIMIT :limit
    """)

    return pd.read_sql(query, engine, params={"limit": limit})


def search_cars(query, limit=100):
    """Search listings by make or model.

    Matches the search term against both Make and Model_No_Year so a
    query like "Toyota" or "Probox" both return results. An empty query
    falls back to a sample of the listings.
    """
    term = (query or "").strip()

    if not term:
        return get_all_cars(limit=limit)

    sql = text("""
        SELECT *
        FROM japan_cars_list
        WHERE "Make" ILIKE :term
           OR "Model_No_Year" ILIKE :term
        ORDER BY "Year" DESC, "Mileage" ASC
        LIMIT :limit
    """)

    return pd.read_sql(
        sql,
        engine,
        params={"term": f"%{term}%", "limit": limit}
    )