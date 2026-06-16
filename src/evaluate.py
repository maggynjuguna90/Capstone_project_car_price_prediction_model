from sklearn.metrics import mean_absolute_error, r2_score

import numpy as np
from sklearn.metrics import mean_absolute_error, r2_score

def evaluate_model(y_true, y_pred, title: str = "Model evaluation") -> dict:
    """
    Evaluates model performance on REAL price scale (recommended)
    """

    # convert log → real price
    y_true_price = np.expm1(y_true)
    y_pred_price = np.expm1(y_pred)

    mae = mean_absolute_error(y_true_price, y_pred_price)
    r2 = r2_score(y_true_price, y_pred_price)

    print(f"\n{title}")
    print("-" * len(title))
    print(f"MAE: ${mae:,.2f}")
    print(f"R² : {r2:.4f}")

    return {
        "mae": mae,
        "r2": r2
    }

def print_observations(metrics: dict):
    """
        Print observations based on modelmetrics
    """
    mae = metrics["mae"]
    r2 = metrics["r2"]

    print("Observations\n")

    print(f"MAE of ${mae} means our model's average prediction is off by ${mae:,.0f} from the true price")

    if r2 > 0.7:
        print(f"r2 score of {r2:.3f} is strong - the model explains {r2 *100}% of the variance in price")
    elif r2 >0.5:
        print(f"r2 of {r2:.3f} is moderate - there is still variance the model cannot capture(Expected for price data)")
    else:
        print(f"r2 of {r2:.3f} is relatively low.This is common for price predictions as many factors are unmeasured")
        