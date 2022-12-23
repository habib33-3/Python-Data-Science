import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

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

scores = cross_val_score(model, X_train, y_train, scoring="neg_mean_squared_error", cv=5)

print(f"score={scores}")

mean_score = abs(scores.mean())
print(f"Mean Score={mean_score}")

model2 = Ridge(alpha=1)
scores2 = cross_val_score(model2, X_train, y_train, scoring="neg_mean_squared_error", cv=5)
mean_score2 = abs(scores2.mean())
print(f"Mean Score2={mean_score2}")

model2.fit(X_train, y_train)
y_final_prediction = model2.predict(X_test)
MSE = mean_squared_error(y_test, y_final_prediction)
print(f"MSE={MSE}")
