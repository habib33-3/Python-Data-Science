import pandas as pd

MyIndex = ['USA', 'Canada', 'Mexico']
MyData = [1776, 1867, 1821]

MySeries = pd.Series(data=MyData, index=MyIndex)
print(MySeries)
