import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import PolynomialFeatures

df = pd.read_csv("../../Files/Advertising.csv")

print(df.head)

X = df.drop("sales", axis=1)
y = df["sales"]

polynomial_converter = PolynomialFeatures(degree=2, include_bias=False)

polynomial_converter.fit(X)

poly_feature = polynomial_converter.transform(X)
print(poly_feature)
