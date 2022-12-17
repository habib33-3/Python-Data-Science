import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

df = pd.read_csv("../../Files/Advertising.csv")

print(df.head)

X = df.drop("sales", axis=1)
y = df["sales"]

polynomial_converter = PolynomialFeatures(degree=2, include_bias=False)

polynomial_converter.fit(X)

poly_feature = polynomial_converter.transform(X)
print(poly_feature)

X_train, X_test, y_train, y_test = train_test_split(poly_feature, y, test_size=0.3, random_state=21)

model = LinearRegression()

model.fit(X_train, y_train)

test_predictions = model.predict(X_test)

# print(f"Coefficient = {model.coef_}")

MAE = mean_absolute_error(y_test, test_predictions)
MSE = mean_squared_error(y_test, test_predictions)
RMSE = np.sqrt(MSE)

print(f"Mean Absolute Error = {MAE}")
print(f"Mean Squared Error = {MSE}")
print(f"Root Mean Squared Error = {RMSE}")
