# Task 11: Final AIML Project Development

# Project Title

**Project Budget Prediction Web Application Using Machine Learning and Streamlit**

---

# 1. Project Overview

The Project Budget Prediction Web Application is a Machine Learning-based system developed to estimate the budget of a software project. The application uses project-related information such as project size, team size, and project duration to predict the expected project budget.

A Random Forest Regression model is trained on a sample dataset and deployed through Streamlit, providing an easy-to-use web interface for users.

---

# 2. Problem Statement

Organizations often need budget estimates before starting a project. Manual estimation can be inaccurate and time-consuming. This project automates the budget estimation process using Machine Learning techniques, helping users make quick and data-driven decisions.

---

# 3. Objectives

The main objectives of this project are:

* Develop a Machine Learning model for budget prediction.
* Create a user-friendly web application using Streamlit.
* Allow users to enter project details and receive instant predictions.
* Demonstrate the deployment of a trained Machine Learning model.

---

# 4. Technologies Used

| Technology   | Purpose                     |
| ------------ | --------------------------- |
| Python       | Programming Language        |
| Pandas       | Data Processing             |
| Scikit-Learn | Machine Learning Model      |
| Joblib       | Model Saving and Loading    |
| Streamlit    | Web Application Development |

---

# 5. Dataset Description

The dataset contains project-related information used for training the prediction model.

| Feature         | Description                            |
| --------------- | -------------------------------------- |
| Project_Size    | Size of the project                    |
| Team_Size       | Number of team members                 |
| Duration_Months | Project duration in months             |
| Budget          | Total project budget (Target Variable) |

### Sample Dataset

| Project_Size | Team_Size | Duration_Months | Budget |
| ------------ | --------- | --------------- | ------ |
| 100          | 5         | 3               | 50000  |
| 150          | 6         | 4               | 70000  |
| 200          | 8         | 5               | 90000  |
| 250          | 10        | 6               | 120000 |
| 300          | 12        | 8               | 150000 |

---

# 6. Machine Learning Model

### Algorithm Used

**Random Forest Regressor**

### Why Random Forest?

* Handles complex relationships effectively.
* Produces accurate predictions.
* Reduces overfitting through multiple decision trees.
* Works well on small datasets.

### Input Features

* Project_Size
* Team_Size
* Duration_Months

### Target Variable

* Budget

---

# 7. Project Structure

```text
Project_Budget_Prediction/
│
├── app.py
├── model.pkl
├── budget_dataset.csv
├── requirements.txt
└── README.md
```

### File Description

**app.py**

* Main Streamlit web application.

**model.pkl**

* Trained Random Forest model.

**budget_dataset.csv**

* Dataset used for training.

**requirements.txt**

* Required Python libraries.

**README.md**

* Project documentation.

---

# 8. Application Workflow

1. User enters project details.
2. Input data is collected through Streamlit.
3. Trained model receives the input.
4. Machine Learning model predicts the budget.
5. Predicted budget is displayed on the screen.

---

# 9. Installation Steps

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 2: Run Application

```bash
streamlit run app.py
```

### Step 3: Open Browser

Streamlit will generate a local URL such as:

```text
http://localhost:8501
```

Open the URL in your browser.

---

# 10. How to Use the Application

1. Enter Project Size.
2. Enter Team Size.
3. Enter Duration in Months.
4. Click **Predict Budget**.
5. View the estimated project budget.

---

# 11. Output

The application displays:

* Predicted Project Budget
* Success Message
* Model Explanation Section

Example Output:

```text
Estimated Budget: $120,000
```

---

# 12. Future Enhancements

* Use larger real-world datasets.
* Add project category selection.
* Include cost visualization charts.
* Improve prediction accuracy.
* Deploy application on Streamlit Cloud.

---

# 13. Conclusion

This project demonstrates the complete Machine Learning workflow, including dataset creation, model training, model serialization, web application development, and deployment using Streamlit. The system successfully predicts project budgets based on project characteristics and provides an easy-to-use interface for end users.

---

# 14. Author

**Final AIML Project Development**

Submitted as part of the AIML Internship Program.

---

# 15. License

This project is developed for educational and learning purposes only.
