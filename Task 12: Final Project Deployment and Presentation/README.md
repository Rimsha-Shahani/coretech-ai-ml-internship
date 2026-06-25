# Smart House Price Prediction System

## Final AI/ML Project

### Project Overview

The Smart House Price Prediction System is a Machine Learning web application developed using Python and Streamlit. The application predicts the estimated price of a house based on the area and number of bedrooms entered by the user.

This project demonstrates the complete Machine Learning workflow including data preprocessing, exploratory data analysis (EDA), model training, model evaluation, and deployment using Streamlit.

---

## Problem Statement

House buyers and sellers often need an estimated market value of a property. The objective of this project is to predict house prices using Machine Learning based on house characteristics.

---

## Dataset Description

The dataset contains the following features:

| Feature  | Description                   |
| -------- | ----------------------------- |
| Area     | House area in square feet     |
| Bedrooms | Number of bedrooms            |
| Price    | House price (Target Variable) |

### Sample Data

| Area | Bedrooms | Price  |
| ---- | -------- | ------ |
| 1000 | 2        | 200000 |
| 1200 | 2        | 250000 |
| 1500 | 3        | 320000 |
| 1800 | 3        | 400000 |
| 2000 | 4        | 480000 |
| 2500 | 4        | 600000 |

---

## Data Preprocessing

The following preprocessing steps were performed:

* Removed duplicate records
* Checked missing values
* Filled missing values using mean values
* Prepared dataset for model training

---

## Exploratory Data Analysis (EDA)

The following visualizations were created:

1. Price Distribution Histogram
2. Area vs Price Scatter Plot
3. Price Box Plot
4. Correlation Heatmap
5. Pair Plot Analysis

These charts help understand relationships between variables and house prices.

---

## Machine Learning Model

### Algorithm Used

Linear Regression

### Input Features

* Area
* Bedrooms

### Output

* Predicted House Price

---

## Model Evaluation

The model was evaluated using:

* Mean Absolute Error (MAE)
* R² Score

These metrics help measure prediction accuracy.

---

## Streamlit Web Application

Features:

* User-friendly interface
* Enter house area
* Enter number of bedrooms
* Instant house price prediction
* Real-time results

---

## Project Structure

Final_Project/

├── dataset.csv

├── preprocessing.py

├── eda.py

├── model_training.py

├── model.pkl

├── app.py

├── requirements.txt

└── README.md

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Streamlit
* Joblib

---

## Installation

### Install Required Libraries

pip install -r requirements.txt

### Train Model

python model_training.py

### Run Streamlit App

streamlit run app.py

---

## Working Process

1. Load Dataset
2. Perform Data Preprocessing
3. Analyze Data using EDA
4. Train Linear Regression Model
5. Save Model using Joblib
6. Load Model in Streamlit App
7. Take User Input
8. Predict House Price
9. Display Result

---

## Conclusion

This project successfully predicts house prices using Machine Learning techniques. The model is deployed through a Streamlit web application, allowing users to easily estimate house prices by entering basic house information.

---

## Author

Rimsha Shahani

AI/ML Final Project Submission
https://www.loom.com/share/eab3a04dc9e440958215d9495377e8e9
