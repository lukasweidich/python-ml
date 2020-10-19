from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, './Salary_Data.csv')
dataset = pd.read_csv(filename)

X = dataset.iloc[:, : -1].values
y = dataset.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1)

# training linear regression model with the training set
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# predicting the test set results
# y_pred = regressor.predict(X_test)
# print(y_pred)

plt.scatter(X_train, y_train, color="red")
plt.plot(X_train, regressor.predict(X_train), color="blue")
plt.title("Salary vs. Experience (Training Set)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary in USD")
# plt.show()

plt.scatter(X_test, y_test, color="red")
plt.plot(X_train, regressor.predict(X_train), color="blue")
plt.title("Salary vs. Experience (Test Set)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary in USD")
# plt.show()

# bonus:
# 1: how to predict salary of employee with 12 years of experience?
twelveYrExperienceSalary = regressor.predict([[12]])
# print(twelveYrExperienceSalary)
# 2: How to get final linear regression expression?
coef = regressor.coef_
intercept = regressor.intercept_
print(coef)
print(intercept)
# function: Salary = 9332.94 * YearsExperience + 25609.89
