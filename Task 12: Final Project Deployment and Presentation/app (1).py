
import streamlit as st
import joblib
import numpy as np

model = joblib.load("model.pkl")

st.title("House Price Prediction App")

area = st.number_input("Area")
bedrooms = st.number_input("Bedrooms")

if st.button("Predict"):
    prediction = model.predict(np.array([[area, bedrooms]]))
    st.success(f"Predicted Price: ${prediction[0]:,.2f}")

st.write("Model: Linear Regression")
