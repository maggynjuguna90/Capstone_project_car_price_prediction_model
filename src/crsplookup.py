import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://postgres:maggy123@localhost:5432/japancars"
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
    except:
        return 0.0