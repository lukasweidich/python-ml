from sklearn.linear_model import LinearRegression
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, './50_Startups.csv')
dataset = pd.read_csv(filename)

X = dataset.iloc[:, : -1].values
y = dataset.iloc[:, -1].values

ct = ColumnTransformer(
    transformers=[('encoder', OneHotEncoder(), [3])], remainder='passthrough')
X = np.array(ct.fit_transform(X))
# print(X)

# in multiple linear regression, there is no need for feature scaling because there are coefficents for every feature

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1)

regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)
np.set_printoptions(precision=2)
# print(np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)), axis=1))

# bonus
# 1: make a single prediction for certain features
singlePrediction = regressor.predict([[1.0, 0.0, 0.0, 160000, 130000, 300000]])
print(singlePrediction)
# 2: get final coefficients
print(regressor.coef_)  # -> returns an array of coef
print(regressor.intercept_)
