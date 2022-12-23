import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("../Files/Advertising.csv")
print(df.head())

X = df.drop("sales", axis=1)
y = df["sales"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

scaler = StandardScaler()

scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

model = Ridge(alpha=100)
model.fit(X_train, y_train)

y_prediction = model.predict(X_test)

MSE = mean_squared_error(y_test, y_prediction)
print(f"Mean squared error={MSE}")

model_two = Ridge(alpha=1)
model_two.fit(X_train, y_train)
y_prediction_two = model_two.predict(X_test)
MSE_two = mean_squared_error(y_test, y_prediction_two)
print(f"Mean squared error for model 2={MSE_two}")
