# Task 10 - AI Model Deployment with Streamlit

## Project Overview

This project demonstrates the deployment of a Machine Learning model using Streamlit. The application predicts the price of a house based on user-provided inputs such as area and number of bedrooms. The model is trained using Linear Regression and saved using Joblib.

The main objective of this project is to create an interactive web application where users can enter house details and instantly receive a predicted house price.

---

## Objectives

* Build a Machine Learning prediction model.
* Save the trained model using Joblib.
* Create a user-friendly web interface using Streamlit.
* Accept user inputs through a form.
* Display prediction results.
* Provide a simple explanation of the model.

---

## Dataset

A sample dataset is used for training the model.

| Area (sq ft) | Bedrooms | Price ($) |
| ------------ | -------- | --------- |
| 1000         | 2        | 200000    |
| 1200         | 2        | 250000    |
| 1500         | 3        | 300000    |
| 1800         | 3        | 350000    |
| 2000         | 4        | 400000    |
| 2500         | 4        | 500000    |

### Features

* Area
* Bedrooms

### Target Variable

* Price

---

## Machine Learning Model

The project uses the **Linear Regression** algorithm from Scikit-Learn.

Linear Regression is a supervised learning algorithm that predicts a continuous value based on input features.

### Why Linear Regression?

* Simple and easy to understand.
* Suitable for numerical prediction tasks.
* Fast training and prediction.
* Works well with small datasets.

---

## Model Training Process

1. Import required libraries.
2. Create the dataset using Pandas.
3. Separate features and target variable.
4. Train the Linear Regression model.
5. Save the trained model using Joblib.
6. Load the saved model for prediction.

---

## Streamlit Application Features

### User Input Form

The application allows users to enter:

* House Area
* Number of Bedrooms

### Prediction Button

After entering values, users can click the **Predict Price** button.

### Output Display

The application displays the predicted house price in a user-friendly format.

### Model Explanation

A brief explanation is provided to help users understand how the prediction model works.

---

## Technologies Used

* Python
* Streamlit
* Pandas
* Scikit-Learn
* Joblib

---

## Project Files

### app.py

Contains the complete Streamlit web application code.

### model.pkl

Stores the trained Linear Regression model.

### requirements.txt

Contains all required Python packages.

### README.md

Project documentation.

---

## Installation Guide

### Step 1: Clone the Repository

```bash
git clone <repository-link>
```

### Step 2: Open Project Folder

```bash
cd Task10
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
streamlit run app.py
```

---

## Sample Prediction

### Input

Area = 1800

Bedrooms = 3

### Output

Predicted Price = $350,000

---

## Future Improvements

* Use a larger real-world dataset.
* Add more features such as location and bathrooms.
* Improve user interface design.
* Deploy the application online using Streamlit Cloud.

---

## Conclusion

This project successfully demonstrates how to deploy a Machine Learning model using Streamlit. Users can provide house information and receive instant price predictions through a simple and interactive web interface.

---
