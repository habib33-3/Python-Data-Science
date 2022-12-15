import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split

df = pd.read_csv("../Files/Advertising.csv")

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

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

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

plt.show()
