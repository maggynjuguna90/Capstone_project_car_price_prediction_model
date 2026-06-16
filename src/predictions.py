import joblib
import pandas as pd
import numpy as np

model = joblib.load("models/car_price_pipeline.pkl")


def predict_japan_price(
    Make,
    Model_no_year,
    Mileage,
    Year,
    Engine_size,
    Transmission_type
):
    features = {
        "Make": Make,
        "Model_No_Year": Model_no_year,
        "Mileage": Mileage,
        "Year": Year,
        "Engine_size": Engine_size,
        "Transmission_type": Transmission_type
    }

    df = pd.DataFrame([features])

    log_price = model.predict(df)[0]

    actual_price = np.expm1(log_price)

    return float(actual_price)