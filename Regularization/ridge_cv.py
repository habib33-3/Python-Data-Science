import numpy as np
import pandas as pd
from sklearn.linear_model import RidgeCV
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("../Files/Advertising.csv")

X = df.drop("sales", axis=1)
y = df["sales"]

polynomial_converter = PolynomialFeatures(degree=3, include_bias=False)
poly_features = polynomial_converter.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(poly_features, y, test_size=0.3, random_state=21)

scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

ridge_cv_model = RidgeCV(alphas=(0.1, 1.0, 10.0), scoring="neg_mean_absolute_error")
ridge_cv_model.fit(X_train, y_train)

best_alpha = ridge_cv_model.alpha_
print(f"Alpha={best_alpha}")

test_prediction_cv_model = ridge_cv_model.predict(X_test)
MAE = mean_absolute_error(y_test, test_prediction_cv_model)
MSE = mean_squared_error(y_test, test_prediction_cv_model)
RMSE = np.sqrt(MSE)

print(f"Prediction={test_prediction_cv_model}")
print(f"Mean Absolute Error= {MAE}")
print(f"Mean Squared Error= {MSE}")
print(f"Root Mean Squared Error= {RMSE}")
