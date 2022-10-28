import pandas as pd

registrations = pd.DataFrame({'reg_id': [1, 2, 3, 4], 'name': ['Andrew', 'Bobo', 'Claire', 'David']})
logins = pd.DataFrame({'log_id': [1, 2, 3, 4], 'name': ['Xavier', 'Andrew', 'Yolanda', 'Bobo']})

print(registrations)
print(logins)

x = pd.merge(left=registrations, right=logins, how="right", on="name")
print(x)
