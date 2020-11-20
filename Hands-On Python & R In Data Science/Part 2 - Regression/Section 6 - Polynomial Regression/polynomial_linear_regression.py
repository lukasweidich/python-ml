from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, './Position_Salaries.csv')
dataset = pd.read_csv(filename)

X = dataset.iloc[:, : -1].values
y = dataset.iloc[:, -1].values
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1)
