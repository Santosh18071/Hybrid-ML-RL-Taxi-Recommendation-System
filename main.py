from hybrid_model import hybrid_score
from recommendation import recommend_taxis
from eta_calculation import calculate_eta
from preprocessing import load_data
from feature_engineering import create_features
from demand_prediction import train_model

# Load dataset
df = load_data(
    "dataset/yellow_tripdata_2024-01.parquet"
)

# Feature Engineering
df = create_features(df)

# Train Model
model, X_test, y_test = train_model(df)

# Predictions
predictions = model.predict(X_test)

# Show first 10 predictions
print(predictions[:10])

print("Before ETA")

distance = 2.5

print("Distance =", distance)

eta = calculate_eta(distance)

print("ETA =", eta, "minutes")

print("After ETA")
print()

print("Top Recommended Taxis")

print(
    recommend_taxis()
)
print()

print("Final Hybrid Recommendations")

print(hybrid_score())