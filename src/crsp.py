import os
import pandas as pd

from sqlalchemy import create_engine


DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:maggy123@localhost:5432/japancars"
)

engine = create_engine(DATABASE_URL)

crsp_df = pd.read_csv(
    "data/NewKRA_CRSP_2025.csv",
    encoding="latin1"
)

crsp_df.columns = crsp_df.columns.str.strip()

print(crsp_df.columns.tolist())

crsp_df.to_sql(
    "crsp_2025_values",
    engine,
    if_exists="replace",
    index=False
)

print("CRSP data loaded successfully.")