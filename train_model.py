"""Train the ice cream sales model and save it. Run: python train_model.py"""
import joblib
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

FEATURES = ["temperature_c", "is_weekend", "rainfall_mm"]  # last two are new
MODEL_FILE = "ice_cream_model.joblib"


def make_data(n=400, seed=42):
    rng = np.random.default_rng(seed)
    temp = rng.uniform(5, 38, n)
    weekend = rng.integers(0, 2, n)
    rain = np.where(rng.random(n) < 0.3, rng.uniform(1, 25, n), 0.0)
    sales = 20 + 6.5 * temp + 45 * weekend - 2.2 * rain + rng.normal(0, 15, n)
    return pd.DataFrame({"temperature_c": temp.round(1), "is_weekend": weekend,
                         "rainfall_mm": rain.round(1), "sales": sales.clip(min=0).round(0)})


def train(df):
    X_tr, X_te, y_tr, y_te = train_test_split(df[FEATURES], df["sales"], test_size=0.2, random_state=1)
    model = LinearRegression().fit(X_tr, y_tr)
    return model, r2_score(y_te, model.predict(X_te))


if __name__ == "__main__":
    df = make_data()
    df.to_csv("ice_cream_data.csv", index=False)
    model, r2 = train(df)
    joblib.dump(model, MODEL_FILE)
    print(f"Saved {MODEL_FILE}. Test R2 = {r2:.3f}")
    print(dict(zip(FEATURES, model.coef_.round(2))))
