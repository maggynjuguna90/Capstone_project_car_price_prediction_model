import pandas as pd 
import numpy as np


TARGET = "log_price"

TARGET_ENCODE_COLS = ["Model_No_Year","Make"]

ONE_HOT_COLS= ["Transmission_type"]

NUMERIC_COLS = [
    "Mileage",
    "Engine_size",
    "Year"
]

def clean_mileage(series: pd.Series)->pd.Series:
    series = series.copy()
    series = pd.to_numeric(series,errors="coerce")
    return series

def clean_engine_size(series: pd.Series)->pd.Series:
    series = series.copy()
    series = pd.to_numeric(series,errors="coerce")
    return series


def clean_year(series:pd.Series)->pd.Series:
    series= series.copy()
    series = pd.to_numeric(series,errors="coerce")
    return series


def clean_transmission_type(series:pd.Series)->pd.Series:
    return series

def clean_model_no_year(series:pd.Series)->pd.Series:
    return series

def clean_make(series:pd.Series)->pd.Series:
    return series


def load_and_clean(filepath: str)-> pd.DataFrame:
    df = pd.read_csv(filepath)
    df["log_price"] = np.log1p(df["Price"])

    #2. Check whether the feature and target columns exist
    cols_needed = TARGET_ENCODE_COLS +ONE_HOT_COLS + NUMERIC_COLS+ ["Price","log_price"]
    cols_available = [c for c in cols_needed if c in df.columns]

    missing_cols = set(cols_needed ) - set(cols_available)
    if missing_cols:
        print(f"Columns not found in dataset: {missing_cols}")
    df = df[cols_available.copy()]
    print(f"Selected {len(cols_available)} columns,expecting 7")

    #cleaning other columns
    if "Mileage" in df.columns:
        df["Mileage"] =clean_mileage(df["Mileage"])

    if "Engine_size" in df.columns:
        df["Engine_size"] = clean_engine_size(df["Engine_size"])

    if "Year" in df.columns:
        df["Year"] = clean_year(df["Year"])

    if "Transmission_type" in df.columns:
        df["Transmission_type"] = clean_transmission_type(df["Transmission_type"])

    if "Model_No_Year" in df.columns:
        df["Model_No_Year"]= clean_model_no_year(df["Model_No_Year"])

    if "Make" in df.columns:
        df["Make"] = clean_make(df["Make"])

    df = df.dropna(how ="all")


    print(f"Clean data shape :{df.shape}")
    print(f"Missing values per column: \n {df.isna().sum().to_string()} \n")

    return df


def get_feature_columns():
    """
    Returns:
        target_encoded_columns,
        one_hot_columns,
        numeric_columns
    """
    return (
        TARGET_ENCODE_COLS,
        ONE_HOT_COLS,
        NUMERIC_COLS
    )