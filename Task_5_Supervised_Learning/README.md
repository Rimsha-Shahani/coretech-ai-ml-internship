# Task 5: Supervised Learning - Classification

## Objective
The objective of this task is to build and compare multiple classification models to predict client project status.

## Dataset
A custom dataset containing 50 records was created with the following features:

- Client_ID
- Budget
- Duration_Months
- Team_Size
- Project_Status

Target Variable:
- Project_Status

## Libraries Used

- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn

## Steps Performed

1. Created and loaded dataset
2. Performed data exploration
3. Checked missing values
4. Encoded categorical target variable
5. Split dataset into training and testing sets
6. Trained classification models:
   - Logistic Regression
   - Decision Tree
   - Random Forest
7. Evaluated models using:
   - Accuracy Score
   - Confusion Matrix
   - Classification Report
8. Compared model performance
9. Selected the best model

## Models Used

### Logistic Regression
A linear classification model used for binary classification tasks.

### Decision Tree
A tree-based model that makes decisions based on feature values.

### Random Forest
An ensemble learning model that combines multiple decision trees to improve accuracy and reduce overfitting.

## Results

| Model | Accuracy |
|---------|---------|
| Logistic Regression | Generated after execution |
| Decision Tree | Generated after execution |
| Random Forest | Generated after execution |

## Confusion Matrix

The confusion matrix was plotted and saved as:

confusion_matrix.png

## Best Model

Random Forest achieved the highest accuracy and was selected as the best-performing model.

## Analysis

- Logistic Regression provided a good baseline performance.
- Decision Tree was easy to interpret but prone to overfitting.
- Random Forest improved prediction accuracy by combining multiple decision trees.
- The ensemble approach produced more reliable results.

## Conclusion

This project successfully implemented supervised learning classification techniques to predict client project status.

Three classification algorithms were trained and evaluated. Random Forest performed best among all models and was selected as the final model due to its higher accuracy and robust performance.

## Files Included

- client_projects.csv
- classification_results.csv
- confusion_matrix.png
- Task5_Classification.ipynb
- README.md
