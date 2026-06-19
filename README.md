# Japan Car Import Comparison

This project helps Kenyan buyers compare the cost of buying a car locally versus
importing it from Japan. A machine learning model predicts the Japan market price,
which is combined with Kenyan market data (shipping cost, KRA taxes) to recommend
whether to import or buy locally. It focuses on car models manufactured from 2018
onwards.

## Objectives

1. Predict Japan car prices.
2. Calculate the cost of importing cars to Kenya.
3. Compare the import cost versus the local market price.
4. Recommend the best option (import or buy locally).

## How it works

The user searches the listings (or enters car details manually: make, model, year,
mileage, engine size, transmission, fuel type, body type). The ML model predicts the
Japan market price. The system then calculates shipping cost and import taxes (import
duty, excise, VAT, IDF, RDL), compares the total import cost against the Kenyan market
price, and recommends whether to import or buy locally.

## Datasets

- Japanese car listings (SBT Japan, BE Forward) → `data/japancars_cleaned.csv`
- Kenyan market price estimates (Jiji Cars, Peach Cars) → `data/local_car_prices.csv`
- KRA import duty guidelines / CRSP 2025 → `data/NewKRA_CRSP_2025.csv`

---

## Getting started

### Prerequisites

- **Python 3.10+** (developed on 3.13)
- **PostgreSQL 12+** running locally
- `git`

### 1. Clone the repository

```bash
git clone https://github.com/maggynjuguna90/Capstone_project_car_price_prediction_model.git
cd Capstone_project_car_price_prediction_model
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

Activate it:

```bash
# macOS / Linux
source .venv/bin/activate

# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create the PostgreSQL database

Create an empty database (the loaders create the tables in step 6):

```bash
createdb japancars
```

If your PostgreSQL uses a specific superuser/password, pass it explicitly, e.g.:

```bash
createdb -U postgres -h localhost japancars
```

### 5. Configure your database credentials

Create a `.env` file in the project root with your local PostgreSQL connection
details:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=japancars
DB_USER=your_postgres_user
DB_PASSWORD=your_postgres_password
```

All database access is centralised in `src/db.py`, which reads these variables.
(Optionally, set `DATABASE_URL` to override the assembled connection string.)

### 6. Populate the database

Run the three loader scripts **from the project root** (they read CSVs from `data/`).
Each rebuilds its table, so they are safe to re-run:

```bash
python src/loaddb.py             # japan_cars_list      (Japan listings)
python src/crsp.py               # crsp_2025_values     (KRA CRSP values)
python src/load_kenya_prices.py  # kenya_market_prices  (Kenya local prices)
```

### 7. Run the app

```bash
python src/app.py
```

Then open:

```
http://127.0.0.1:5001
```

> **Port note:** the app runs on **5001** by default. On macOS, port 5000 is used by
> the AirPlay Receiver, so 5001 avoids that conflict. To use a different port, set the
> `PORT` environment variable, e.g. `PORT=8000 python src/app.py`.

---

## Using the app

| Route       | Description                                                        |
|-------------|--------------------------------------------------------------------|
| `/`         | Home page                                                          |
| `/search`   | Search listings by make or model, then compare                    |
| `/cars`     | Browse available listings                                          |
| `/manual`   | Enter car details manually (for cars not in the listings)         |
| `/compare`  | Comparison result: predicted price, tax breakdown, recommendation |

Typical flow: go to **`/search`**, search for a car (e.g. "Toyota" or "Probox"),
click **Compare** on a result, and view the import-vs-local breakdown. If a car is
not listed, use **`/manual`** to enter its details.

## Project structure

```
.
├── data/                 # Source CSV datasets
├── models/               # Trained ML pipeline (car_price_pipeline.pkl)
├── notebooks/            # Exploratory analysis
├── src/
│   ├── app.py            # Flask app and routes
│   ├── db.py             # Central database configuration
│   ├── loaddb.py         # Loader: japan_cars_list
│   ├── crsp.py           # Loader: crsp_2025_values
│   ├── load_kenya_prices.py  # Loader: kenya_market_prices
│   ├── enrich.py         # Derives Fuel_Type / Body_Type for listings
│   ├── carlisting.py     # Listing queries (browse / search)
│   ├── predictions.py    # ML price prediction
│   ├── comparison.py     # Import-vs-local comparison logic
│   ├── calculator.py     # KRA tax/duty calculation
│   ├── shippincost.py    # Shipping cost by body type
│   ├── crsplookup.py     # CRSP value lookup
│   ├── kenyanlocal_prices.py  # Kenya market price lookup
│   └── templates/        # HTML templates
└── requirements.txt
```

## Troubleshooting

- **`ModuleNotFoundError`** — ensure the virtual environment is activated and
  `pip install -r requirements.txt` completed.
- **`database "japancars" does not exist`** — run step 4 (`createdb japancars`).
- **`relation "japan_cars_list" does not exist`** — run the loaders in step 6.
- **`connection refused` / auth errors** — confirm PostgreSQL is running and the
  credentials in `.env` are correct.
- **Run scripts from the project root** so the relative `data/` and `models/` paths
  resolve correctly.
