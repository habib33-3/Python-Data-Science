import pandas as pd

q1 = {
    'Japan': 80,
    'China': 450,
    'India': 200,
    'USA': 250
}
q2 = {
    'Brazil': 100,
    'China': 500,
    'India': 210,
    'USA': 260
}

Sales_q1 = pd.Series(q1)
Sales_q2 = pd.Series(q2)

print(f"Sales of q1\n{Sales_q1}")
print()
print(f"Sales of q2\n{Sales_q2}")
print()
print(f"Q1 multiplied by 12 \n{Sales_q1 * 12}")

total = Sales_q1.add(Sales_q2, fill_value=0)
print(total)
