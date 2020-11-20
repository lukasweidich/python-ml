#import libraries
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# be able to use relative imports
import os
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, './Data.csv')

# import dataset
dataset = pd.read_csv(filename)
X = dataset.iloc[:, : -1].values
# : means range, no start and end means all rows
# iloc [index of rows, index of columns]
# range includes lowerbound, excludes upperbound
y = dataset.iloc[:, -1].values
# print(X)
# print(y)

# ways to handle missing data:
# a) remove entry
# b) use average/median/most frequent from column
imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])
# print(X)

# categorical data
# encoding the independet variable
# encode first column, return encoded and remaining content of columns
ct = ColumnTransformer(
    transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
X = np.array(ct.fit_transform(X))
# print(X)

# encoding the dependet variable
le = LabelEncoder()
y = le.fit_transform(y)
# print(y)

# splitting in training and test sets
# no feature scaling before splitting into test and training set to avoid information leakage
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1)

# print(X_train)
# print(X_test)
# print(y_train)
# print(y_test)

# feature scaling is being applied after the split
# why feature scaling? avoid features dominating others and therefore forcing them to not be considered
# used for certain machine learning models, not all
# use normalization for normally distributed data and scaling (standardization) for data that is not normally distributed
sc = StandardScaler()
X_train[:, 3:] = sc.fit_transform(X_train[:, 3:])
X_test[:, 3:] = sc.transform(X_test[:, 3:])
print(X_train)
print(X_test)
