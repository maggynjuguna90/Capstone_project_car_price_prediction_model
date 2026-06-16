import pandas as pd 

df1 = pd.read_csv("cars_prices.csv")
df2 = pd.read_csv("car_prices_4000.csv")

combined = pd.concat([df1,df2],ignore_index=True)

combined.to_csv("japan_cars.csv",index= False)

df = pd.read_csv("japan_cars.csv")
print(df.head())

df["Mileage"] = (
    df["Mileage"]
    .str.replace(",", "", regex=False)
    .str.replace("km", "", regex=False)
    .str.strip())

df["Engine_size"] = (
    df["Engine_size"]
    .str.replace(",", "", regex=False)
    .str.replace("cc", "", regex=False)
    .str.strip()
)

df["Mileage"] = pd.to_numeric(df["Mileage"], errors="coerce")
df["Engine_size"] = pd.to_numeric(df["Engine_size"], errors="coerce")

df["Price"] = (
    df["Price"]
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
    .str.strip()
)

df["Price"] = pd.to_numeric(df["Price"], errors="coerce")



df["Year"] = df["Year"].str.split("/").str[0]
df["Year"] = pd.to_numeric(df["Year"], errors="coerce")

print(df.eq("n/a").sum())

df = df.dropna(subset=["Price"])
df["Mileage"] = df["Mileage"].fillna(df["Mileage"].median())
df["Engine_size"] = df["Engine_size"].fillna(df["Engine_size"].median())
df["Year"] = df["Year"].fillna(df["Year"].median())

print(df.head())



df = df.dropna(subset=["Transmission_type"])
print(df.isnull().sum())

print(df.info())
print(df.describe())
print(df.head())


#df.to_csv("japan_cars_cleaned.csv", index=False)

from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("postgresql://postgres:maggy123@localhost:5432/japancars")

df = pd.read_sql("SELECT current_database();",engine)

print(df)

df = pd.read_csv("../japancars_cleaned.csv")

df.to_sql("japan_cars", engine,if_exists="replace",index=False)

print("Data loaded successfully")

df3 = pd.read_csv("../local_car_prices.csv")
print(df.head())

from sqlalchemy import create_engine
import pandas as pd

# Connect to PostgreSQL
engine = create_engine(
    "postgresql://postgres:maggy123@localhost:5432/japancars"
)

# Load CSV file
df3 = pd.read_csv("../local_car_prices.csv")

# Clean column names (important for ML projects)
df3.columns = df3.columns.str.lower().str.replace(" ", "_")

# Upload to database
df3.to_sql(
    "kenya_market_prices",
    engine,
    if_exists="replace",
    index=False
)

print("Data successfully uploaded to PostgreSQL!")