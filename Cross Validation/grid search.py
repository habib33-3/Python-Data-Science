import pandas as pd
from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV
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

base_elastic_model = ElasticNet()
parameter_grid = {
    "alpha": [0.1, 1, 5, 10, 50, 100],
    "l1_ratio": [0.1, 0.5, 0.7, 0.95, 0.99, 1]
}

grid_model = GridSearchCV(estimator=base_elastic_model, param_grid=parameter_grid, scoring="neg_mean_squared_error",
                          verbose=2)

grid_model.fit(X_train, y_train)

best_model = grid_model.best_estimator_
print(f"best model = {best_model}")

result = pd.DataFrame(grid_model.cv_results_)
print(result)

y_prediction = grid_model.predict(X_test)

MSE = mean_squared_error(y_test, y_prediction)
print(f"MSE = {MSE}")
