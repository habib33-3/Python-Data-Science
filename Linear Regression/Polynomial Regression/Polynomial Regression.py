import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from joblib import dump, load
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures

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

train_rmse_error = []
test_rmse_error = []

for d in range(1, 10):
    poly_converter = PolynomialFeatures(degree=d, include_bias=False)
    poly_feature = poly_converter.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(poly_feature, y, test_size=0.3, random_state=21)

    model = LinearRegression()
    model.fit(X_train, y_train)

    train_predict = model.predict(X_train)
    test_predict = model.predict(X_test)

    train_rmse = np.sqrt(mean_squared_error(y_train, train_predict))
    test_rmse = np.sqrt(mean_squared_error(y_test, test_predict))

    train_rmse_error.append(train_rmse)
    test_rmse_error.append(test_rmse)

print(f"Train RMSE Error = {train_rmse_error}")
print(f"Test RMSE Error = {test_rmse_error}")

plt.plot(range(1, 6), train_rmse_error[:5], label="Train RMSE")
plt.plot(range(1, 6), test_rmse_error[:5], label="Test RMSE")

plt.xlabel("Degree of Polynomial")
plt.ylabel("RMSE")

plt.legend()

final_poly_converter = PolynomialFeatures(degree=2, include_bias=False)

final_model = LinearRegression()

fully_converted_X = final_poly_converter.fit_transform(X)
final_model.fit(fully_converted_X, y)

dump(final_model, "final_poly_model.joblib")

dump(final_poly_converter, "final_poly_converter.joblib")

loaded_converter = load("final_poly_converter.joblib")
loaded_model = load("final_poly_model.joblib")

campaign = [[149, 22, 12]]
transformed_data = loaded_converter.fit_transform(campaign)
prediction = loaded_model.predict(transformed_data)

print(f"Prediction: {prediction}")

plt.show()
