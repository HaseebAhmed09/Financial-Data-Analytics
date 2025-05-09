# -*- coding: utf-8 -*-
"""Linear_Regression_Salary.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1x8lXN9_fyJw9aTur9_S3SxNa7sz5Fiwd

Suppose you are working in Finance Department at a Corporate employer who believes in cost cutting due to inflation and economic slowdown. You are tasked to figure out what is the ideal salary for the future-hires in which company can still ensure employee motivation and also not overpay.

# Task
--- Create a ML model using Linear Regression. Predict the salary based on years of work experience

---

Import Libraries
"""

# Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_squared_error, r2_score
import ipywidgets as widgets
from IPython.display import display

"""Load and Explore Dataset"""

# # Loading the dataset
# file_path = '/content/years_experience_salary_data.csv'  # Updated file path
# df = pd.read_csv(file_path)

# Load Dataset
from google.colab import files
uploaded = files.upload()

import pandas as pd

df = pd.read_csv('/content/years_experience_salary_data (1).csv')  # Adjust filename if needed

# Displaying the first few rows of the dataset
print("First few rows of the dataset:")
print(df.head())

# Checking for null values
print("\nNull values in each column:")
print(df.isnull().sum())

# Descriptive statistics of the dataset
print("\nDescriptive statistics of the dataset:")
print(df.describe())

"""**Exploratory Data Analysis (EDA):**


EDA helps verify the appropriateness of using a linear regression model by identifying patterns and relationships in the data.

It also shows their linear relationship using scatter plots and correlation analysis.


"""

# Visualizing the data distribution
plt.figure(figsize=(14, 5))

# Distribution plot for 'Years Experience'
plt.subplot(1, 2, 1)
sns.histplot(df['Years Experience'], kde=True, bins=20, color='blue')
plt.title('Distribution of Years Experience')

# Distribution plot for 'Salary'
plt.subplot(1, 2, 2)
sns.histplot(df['Salary'], kde=True, bins=20, color='green')
plt.title('Distribution of Salary')

plt.show()

# Box plot for 'Years Experience'
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='Years Experience', color='skyblue')
plt.title('Box Plot of Years Experience')
plt.show()

# Box plot for 'Salary'
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='Salary', color='lightgreen')
plt.title('Box Plot of Salary')
plt.show()

# Scatter plot to visualize the relationship
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Years Experience', y='Salary', data=df, color='purple')
plt.title('Years Experience vs. Salary')
plt.xlabel('Years Experience')
plt.ylabel('Salary')
plt.show()

# Correlation between features
correlation = df.corr()
print("\nCorrelation matrix:")
print(correlation)

# Heatmap for correlation
plt.figure(figsize=(6, 4))
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

"""If the correlation coefficient between "Years Experience" and "Salary" is close to 1, it suggests a strong positive linear relationship, implying that as "Years Experience" increases, "Salary" tends to increase proportionally.



A high correlation coefficient indicates that a linear model is appropriate, while a lower correlation suggests that a linear relationship may not fully capture the dynamics between the variables.




"""



"""**Model Building and Training:**

The chunk below splits the dataset into training and testing sets, builds a linear regression model, trains it on the training data, and makes predictions on the test set.

"""

# Splitting the data into training and testing sets
X = df[['Years Experience']]
y = df['Salary']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Creating the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Making predictions on the test set
y_pred = model.predict(X_test)

# Evaluating the model using R-squared and RMSE
r2 = r2_score(y_test, y_pred)

print(f"R-squared: {r2}")



"""This value indicates that approximately 89.11% of the variance in the dependent variable ("Salary") can be explained by the independent variable ("Years Experience") using this linear regression model.


In simpler terms: "Years Experience" is a strong predictor of "Salary" in your dataset, as the model explains a large portion of the variability in salary.

**Residual Analysis to check for**

Linearity: Relationship between predictors and response is linear.

Independence: Residuals are independent.

Homoscedasticity: Residuals have constant variance.

Normality: Residuals are normally distributed.
"""

# Scatter plot to check linearity
plt.figure(figsize=(8, 6))
plt.scatter(X_test, y_test, color='blue', label='Actual Values')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Fitted Line')
plt.title('Linearity Check: Years Experience vs. Salary')
plt.xlabel('Years Experience')
plt.ylabel('Salary')
plt.legend()
plt.show()

"""Interpretation: If the scatter plot shows a roughly linear relationship between the independent variable ("Years Experience") and the dependent variable ("Salary") with points closely scattered around the fitted line (red), the linearity assumption is satisfied.

"""

#Calculate residuals
residuals = y_test - y_pred

# Calculate residuals
residuals = y_test - y_pred
# Plot residuals over the order of observations to check independence
plt.figure(figsize=(8, 6))
plt.plot(range(len(residuals)), residuals, marker='o', linestyle='', color='blue')
plt.axhline(y=0, color='red', linestyle='--')
plt.title('Independence Check: Residuals over Observations')
plt.xlabel('Observation Order')
plt.ylabel('Residuals')
plt.show()

"""Interpretation: If the plot shows no clear pattern or structure (random scatter), the independence assumption is likely met. Non-random patterns (e.g., trends or cycles) suggest a violation of independence.

"""

# Plot residuals vs. fitted values to check homoscedasticity
plt.figure(figsize=(8, 6))
plt.scatter(y_pred, residuals, color='blue')
plt.axhline(y=0, color='red', linestyle='--')
plt.title('Homoscedasticity Check: Residuals vs. Predicted Values')
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
plt.show()

"""Interpretation: If the residuals are randomly scattered around the horizontal axis (y=0) with a consistent spread, the homoscedasticity assumption is satisfied."""

# Histogram of residuals to check normality
plt.figure(figsize=(8, 5))
sns.histplot(residuals, kde=True, color='purple')
plt.title('Normality Check: Histogram of Residuals')
plt.xlabel('Residuals')
plt.ylabel('Frequency')
plt.show()

# Q-Q plot to further check for normality
import scipy.stats as stats
fig, ax = plt.subplots(figsize=(6, 6))
stats.probplot(residuals, dist="norm", plot=ax)
plt.title('Q-Q Plot of Residuals')
plt.show()

"""Interpretation:

Histogram: If the residuals follow a bell-shaped curve, it suggests they are normally distributed.

Q-Q Plot: If the points lie approximately along the straight line, it indicates that the residuals are normally distributed.

A random scatter around the horizontal line (y = 0) indicates that the linear regression model is appropriate and that the relationship between "Years Experience" and "Salary" is linear.

Meeting all four assumptions (linearity, independence, homoscedasticity, and normality of residuals) ensures the linear regression model provides unbiased and reliable estimates.


If the assumptions are not met, the model may give biased predictions, leading to inaccurate results and incorrect conclusions. In such cases, alternative modeling techniques or data transformations should be considered.

Cross-Validation
"""

# Performing k-fold cross-validation to evaluate model generalizability
cv_scores = cross_val_score(model, X, y, cv=5, scoring='r2')  # Using R-squared as the scoring metric
print(f"Cross-Validation R-squared scores: {cv_scores}")
print(f"Mean Cross-Validation R-squared: {cv_scores.mean()}")

"""This chunk performs 5-fold cross-validation to evaluate the model's generalizability. It splits the dataset into 5 parts and trains/tests the model on these subsets to get multiple R-squared scores.


The mean cross-validation R-squared value indicates how well the model is likely to perform on unseen data, with values close to the initial R-squared indicating a stable and reliable model.


5-fold cross-validation means the dataset is divided into 5 parts, with the model being trained on 4 parts and tested on 1 part in each iteration.


"""

# Interactive Prediction Code
def interactive_prediction(years_exp):
    # Predicting salary for given years of experience
    predicted_salary = model.predict(np.array(years_exp).reshape(-1, 1))[0]
    print(f"For {years_exp} years of experience, the predicted salary is: ${predicted_salary:.2f}")

# Creating an interactive widget
years_exp_widget = widgets.FloatSlider(value=5.0, min=1.0, max=30.0, step=0.1, description='Years Exp:')
interactive_predict_button = widgets.interactive(interactive_prediction, years_exp=years_exp_widget)

print("\nInteractive Salary Prediction:")
display(interactive_predict_button)

"""**Data**

What is the average number of years of experience?

What is the standard deviation of salaries?

What does the minimum and maximum salary suggest about the data?

# Questions


1. How can we interpret the coefficient of "years of experience"? What does a positive coefficient indicate?

2. Why is it important to check the distribution of salary and years of experience before applying regression?

3. What happens if we use all the data for training and none for testing? How does it impact model evaluation?

4. What does it mean if the model's predicted salaries are consistently lower or higher than actual salaries?

5. How does increasing or decreasing the training dataset size affect model performance?

6. If another variable, such as "certifications," is added to the dataset, how might it impact the regression results?

7. If the dataset contained outliers (e.g., a person with 50 years of experience but a very low salary), how would that affect the model?

8. If the dataset only contains a small number of observations, what problems might arise when training the model?

9. How does the LinearRegression().fit() function work in training the model?

10. If the dataset had outliers (e.g., a CEO with 40 years of experience earning $1M), how would that affect the model?

11. If the company wanted to predict salary for interns (0 years experience), would this model still be reliable? Why or why not?
"""

# Answers:
# Q1) Coefficient of 5076.28 tells every additional increase in experience increases this much salary. A positive coeff means direct relation.

# Q2) To check for outliers or skewness or linearity.

# Q3) It could lead to overfitting where model learn the training data and dont perform well on test data

# Q4) If its lower model is underestimating maybe leaving a few a factors, and if high so overestimating

# Q5) Increasing data sets reduce variance and make predictions more reliable and decreasing may result model not compeletely recognising the patterns

# Q6) It may improve the model but it ight also produce multicolinearity with years experience.

# Q7) the model would be skewed making predictions less reliable.

# Q8) With small number of observations data may not perform well to new data points as it might not generalize to training data or it can learn pattern of training data only means overfitting

# Q9) It finds the best line of best fit with leastr squared error.

# Q10) Model would skew towards high salary as it might overestimate salaries. This increases MSE and reduces accuracy.

# Q11) The salary trends for years experience may not fit well for interns or entry level jobs as it migh over or under estimate it.

