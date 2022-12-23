import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("../Files/Advertising.csv")
print(df.head())

X = df.drop("sales", axis=1)
y = df["sales"]

X_train, X_other, y_train, y_other = train_test_split(X, y, test_size=0.3, random_state=101)
X_eval, X_test, y_eval, y_test = train_test_split(X_other, y_other, test_size=0.5, random_state=101)

scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)
X_eval = scaler.transform(X_eval)

model1 = Ridge(alpha=100)
model1.fit(X_train, y_train)

y_eval_predicted = model1.predict(X_eval)
model1_MSE = mean_squared_error(y_eval, y_eval_predicted)

print(f"Model1 MSE: {model1_MSE}")

model2 = Ridge(alpha=1)
model2.fit(X_train, y_train)

y_eval_predicted2 = model2.predict(X_eval)
model2_MSE = mean_squared_error(y_eval, y_eval_predicted2)

print(f"Model2 MSE: {model2_MSE}")

final_prediction = model2.predict(X_test)
final_MSE = mean_squared_error(y_test, final_prediction)
print(f"Final MSE: {final_MSE}")
