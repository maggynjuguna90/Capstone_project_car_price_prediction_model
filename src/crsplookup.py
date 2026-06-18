import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

engine = create_engine(
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


def get_crsp_value(make, model):
    query = """
        SELECT "CRSP (KES.)"
        FROM crsp_2025_values
        WHERE UPPER("Make") = UPPER(%s)
          AND UPPER("Model") = UPPER(%s)
        LIMIT 1
    """

    df = pd.read_sql(query, engine, params=(make, model))

    if df.empty:
        return 0.0

    value = df.iloc[0, 0]

    if isinstance(value, str):
        value = value.replace(",", "")

    try:
        return float(value)
    except ValueError:
        return 0.0