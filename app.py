import joblib
import pandas as pd
import streamlit as st

from train_model import FEATURES, MODEL_FILE, make_data, train

st.set_page_config(page_title="Ice Cream Sales Predictor", page_icon="🍦")


@st.cache_resource
def get_model():
    try:
        return joblib.load(MODEL_FILE)
    except Exception:  # e.g. scikit-learn version mismatch: retrain
        return train(make_data())[0]


model = get_model()

st.title("🍦 Ice Cream Sales Predictor")
st.write("Enter the day's conditions to predict how many ice creams will sell.")

temp = st.slider("Temperature (°C)", 5.0, 38.0, 25.0, 0.5)
weekend = st.radio("Day type", ["Weekday", "Weekend"], horizontal=True)
rain = st.slider("Rainfall (mm)", 0.0, 25.0, 0.0, 0.5, help="0 means a dry day")

X = pd.DataFrame([[temp, 1 if weekend == "Weekend" else 0, rain]], columns=FEATURES)
pred = max(0, float(model.predict(X)[0]))
st.metric("Predicted sales", f"{pred:.0f} ice creams")
st.caption("Model: linear regression on temperature, weekend, and rainfall.")
