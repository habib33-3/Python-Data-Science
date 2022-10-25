import numpy as np
import pandas as pd

np.random.seed(1)
MyData = np.random.randint(1, 101, (4, 3))


MyIndex = ["CA", 'NA', 'AZ', 'TX']
MyColumns = ['Jan', 'Feb', 'Mar']

df = pd.DataFrame(MyData, MyIndex, MyColumns)
print(df)
