from joblib import load

loaded_model = load("final_model.joblib")

campaign = [[149, 22, 12]]
prediction = loaded_model.predict(campaign)

print(f"prediction = {prediction}")
