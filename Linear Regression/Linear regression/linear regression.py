import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from joblib import dump
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split

df = pd.read_csv("../../Files/Advertising.csv")

print(df.head(10))

fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(16, 6))

axes[0].plot(df["TV"], df["sales"], "o")
axes[0].set_ylabel("Sales")
axes[0].set_title("TV Spend")

axes[1].plot(df["radio"], df["sales"], "o")
axes[1].set_ylabel("Sales")
axes[1].set_title("Radio Spend")

axes[2].plot(df["newspaper"], df["sales"], "o")
axes[2].set_ylabel("Sales")
axes[2].set_title("Newspaper Spend")

X = df.drop("sales", axis=1)
y = df["sales"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=21)

model = LinearRegression()
model.fit(X_train, y_train)

test_predictions = model.predict(X_test)

print()
print("prediction=")
print(test_predictions)

print(df["sales"].mean())

plt.figure(2)
sns.histplot(data=df, x="sales")

MeanAError = mean_absolute_error(y_test, test_predictions)
print()
print("Mean Absolute Error=")
print(MeanAError)

MeanSError = mean_squared_error(y_test, test_predictions)
RootMeanSError = np.sqrt(MeanSError)
print()
print("Mean Squared Error=")
print(MeanSError)
print("Root Mean Squared Error=")
print(RootMeanSError)

test_residual = y_test - test_predictions
print(test_residual)

plt.figure(3)
plt.axhline(y=0, color="red", ls="--")
sns.scatterplot(x=y_test, y=test_residual)

final_model = LinearRegression()

final_model.fit(X, y)
print()
print("Coefficient= ")
print(final_model.coef_)

y_hat = final_model.predict(X)
print()
print("y_hat = ")
print(y_hat)

fig2, axes = plt.subplots(nrows=1, ncols=3, figsize=(16, 6))

axes[0].plot(df["TV"], df["sales"], "o")
axes[0].plot(df["TV"], y_hat, "o", color="red")
axes[0].set_ylabel("Sales")
axes[0].set_title("TV Spend")

axes[1].plot(df["radio"], df["sales"], "o")
axes[1].plot(df["radio"], y_hat, "o", color="red")
axes[1].set_ylabel("Sales")
axes[1].set_title("Radio Spend")

axes[2].plot(df["newspaper"], df["sales"], "o")
axes[0].plot(df["newspaper"], y_hat, "o", color="red")
axes[2].set_ylabel("Sales")
axes[2].set_title("Newspaper Spend")

plt.tight_layout()

dump(final_model, "final_model.joblib")

plt.show()
