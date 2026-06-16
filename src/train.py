import os
import sys
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, TargetEncoder
from xgboost import XGBRegressor

from preprocessing import (
    load_and_clean,
    TARGET,
    TARGET_ENCODE_COLS,
    ONE_HOT_COLS,
    NUMERIC_COLS
)

from evaluate import (
    evaluate_model,
    print_observations
)


DATA_PATH = "data/japancars_cleaned.csv"
MODEL_PATH = "models/car_price_pipeline.pkl"
RANDOM_STATE = 42
TEST_SIZE = 0.2

XGB_PARAMS = {
    "n_estimators": 600,
    "max_depth": 6,
    "learning_rate": 0.03,
    "subsample": 0.8,
    "colsample_bytree": 0.8,
    "tree_method": "hist",
    "random_state": RANDOM_STATE,
    "reg_alpha": 0.05,
    "reg_lambda": 1.0
}


def build_preprocessor(num_cols, target_cols, onehot_cols):

    numeric_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])

    target_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", TargetEncoder(
            smooth="auto",
            random_state=RANDOM_STATE
        ))
    ])

    onehot_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore"))
    ])

    preprocessor = ColumnTransformer([
        ("num", numeric_pipeline, num_cols),
        ("target", target_pipeline, target_cols),
        ("onehot", onehot_pipeline, onehot_cols)
    ])

    return preprocessor



def build_pipeline(num_cols, target_cols, onehot_cols):

    preprocessor = build_preprocessor(
        num_cols,
        target_cols,
        onehot_cols
    )

    model = XGBRegressor(**XGB_PARAMS)

    return Pipeline([
        ("preprocessor", preprocessor),
        ("model", model)
    ])



def main():

    print("\nJapan Car Price Prediction - Training\n")

    # 1. Load & clean
    df = load_and_clean(DATA_PATH)

    

    # 2. Split features/target
    X = df[NUMERIC_COLS+ TARGET_ENCODE_COLS+ ONE_HOT_COLS]
    y = df[TARGET]

    print("Feature groups:")
    print("Numeric:", NUMERIC_COLS)
    print("Target encoded:", TARGET_ENCODE_COLS)
    print("One-hot:", ONE_HOT_COLS)

    # 3. Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE
    )

    print(f"\nTraining samples: {len(X_train):,}")
    print(f"Testing samples: {len(X_test):,}\n")

    # 4. Build model
    print("Building pipeline...")
    pipeline = build_pipeline(
        NUMERIC_COLS,
        TARGET_ENCODE_COLS,
        ONE_HOT_COLS
    )

    print("Training model...")
    pipeline.fit(X_train, y_train)
    print("Training complete.\n")

    # 5. Predictions
    y_pred_train = pipeline.predict(X_train)
    y_pred_test = pipeline.predict(X_test)

    train_metrics = evaluate_model(
        y_train,
        y_pred_train,
        title="Training Performance"
    )

    test_metrics = evaluate_model(
        y_test,
        y_pred_test,
        title="Test Performance"
    )

    print_observations(test_metrics)

    

    # 7. Save model
    os.makedirs("models", exist_ok=True)

    joblib.dump(
        pipeline,
        MODEL_PATH
    )

    print(f"\nModel saved → {MODEL_PATH}")
    print("\nTraining complete.\n")


if __name__ == "__main__":
    main()