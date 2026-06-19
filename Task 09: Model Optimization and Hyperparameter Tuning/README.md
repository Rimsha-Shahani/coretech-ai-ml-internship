# Task 09: Model Optimization and Hyperparameter Tuning

## Objective

The objective of this task is to optimize the best machine learning model from previous tasks and improve its performance. Hyperparameter tuning, cross-validation, feature importance analysis, learning curve plotting, and overfitting/underfitting analysis are performed. Finally, the model performance before and after optimization is compared.

---

## Tools and Libraries Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn

---

## Dataset

CoreTech Client Dataset

The dataset was loaded and preprocessed before model training.

---

## Step 1: Data Preprocessing

The following preprocessing steps were performed:

- Loaded dataset using Pandas
- Checked dataset structure
- Handled missing values
- Converted categorical variables into numerical format
- Prepared feature and target variables

---

## Step 2: Train-Test Split

The dataset was divided into:

- 80% Training Data
- 20% Testing Data

This allows the model to learn from training data and evaluate performance on unseen test data.

---

## Step 3: Baseline Model Training

A Random Forest Classifier was selected as the baseline model.

The model was trained using default parameters and initial accuracy was calculated.

### Accuracy Before Optimization

The baseline model achieved an initial accuracy score before applying any optimization techniques.

---

## Step 4: K-Fold Cross Validation

5-Fold Cross Validation was applied to obtain a more reliable estimate of model performance.

### Benefits

- Reduces bias in evaluation
- Uses all data for training and testing
- Produces more reliable results

---

## Step 5: Hyperparameter Tuning

GridSearchCV was used to find the best combination of parameters.

### Parameters Tuned

- n_estimators
- max_depth
- min_samples_split

### Example Parameter Grid

```python
param_grid = {
    'n_estimators':[100,200,300],
    'max_depth':[5,10,15],
    'min_samples_split':[2,5,10]
}
```

GridSearchCV evaluated multiple parameter combinations and selected the best-performing model.

---

## Step 6: Optimized Model Training

The best parameters obtained from GridSearchCV were used to train an optimized Random Forest model.

### Accuracy After Optimization

The optimized model achieved better performance than the baseline model.

---

## Step 7: Performance Comparison

| Metric | Before Optimization | After Optimization |
|----------|----------|----------|
| Accuracy | Initial Score | Improved Score |

The optimized model showed better predictive performance and generalization ability.

---

## Step 8: Feature Importance Analysis

Feature importance was calculated to determine which variables contributed most to the prediction.

### Purpose

- Identify influential features
- Improve model interpretability
- Understand decision-making process

A bar chart of the top important features was generated.

---

## Step 9: Learning Curve Analysis

Learning curves were plotted using training and validation scores.

### Purpose

- Analyze learning behavior
- Detect overfitting
- Detect underfitting
- Evaluate model scalability

---

## Step 10: Overfitting and Underfitting Analysis

### Overfitting

Occurs when:

- Training Accuracy is very high
- Validation Accuracy is significantly lower

Example:

Training Accuracy = 99%

Validation Accuracy = 75%

### Underfitting

Occurs when:

- Training Accuracy is low
- Validation Accuracy is also low

Example:

Training Accuracy = 60%

Validation Accuracy = 58%

### Good Fit

Occurs when:

Training Accuracy = 90%

Validation Accuracy = 88%

Small difference between both scores indicates good generalization.

---

## Step 11: Confusion Matrix

A confusion matrix was generated to evaluate classification performance.

### Purpose

- Analyze correct predictions
- Analyze incorrect predictions
- Evaluate class-wise performance

---

## Step 12: Classification Report

The classification report includes:

- Accuracy
- Precision
- Recall
- F1-Score

These metrics provide detailed insights into model performance.

---

## Results

### Before Optimization

- Random Forest used default parameters
- Moderate prediction performance

### After Optimization

- Best hyperparameters selected using GridSearchCV
- Improved accuracy
- Better model generalization
- Reduced overfitting risk

---

## Conclusion

Model optimization significantly improved performance. By applying GridSearchCV, K-Fold Cross Validation, Feature Importance Analysis, and Learning Curve Analysis, the model became more accurate and reliable. The optimized model achieved better prediction capability and improved generalization on unseen data.



## Author

Rimsha Shahani

BS Computer Science

CoreTech AI/ML Internship
