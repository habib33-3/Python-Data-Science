import pandas as pd

Dictionary1 = {
    "Bangladesh": "Dhaka",
    "India": "Delhi",
    "Nepal": "Kathmandu",
    "Sri Lanka": "Colombo",
    "Pakistan": "Islamabad",
    "UK": "London",
    "USA": "Washington DC"
}

print(pd.Series(Dictionary1))
