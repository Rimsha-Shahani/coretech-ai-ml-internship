
import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model.pkl")

st.title("Project Budget Prediction Web App")

st.write("Enter project details below:")

size = st.number_input("Project Size", min_value=1)

team = st.number_input("Team Size", min_value=1)

duration = st.number_input("Duration (Months)", min_value=1)

if st.button("Predict Budget"):

    input_data = pd.DataFrame(
        [[size,team,duration]],
        columns=[
            "Project_Size",
            "Team_Size",
            "Duration_Months"
        ]
    )

    prediction = model.predict(input_data)

    st.success(
        f"Estimated Budget: ${prediction[0]:,.2f}"
    )

st.subheader("Model Explanation")

st.write(
"This application uses a Random Forest Machine Learning model to predict project budget based on project size, team size and duration."
)
