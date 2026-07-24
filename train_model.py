import os
import pickle

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# Load dataset
df = pd.read_csv("database/diabetes.csv")

X = df.drop("Outcome", axis=1)
y = df["Outcome"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Scale data
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train model
model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

# Create models folder if it doesn't exist
os.makedirs("models", exist_ok=True)

# Save model
with open("models/diabetes_model.pkl", "wb") as f:
    pickle.dump(model, f)

# Save scaler
with open("models/scaler_model.pkl", "wb") as f:
    pickle.dump(scaler, f)

print("Model saved successfully!")
print("Scaler saved successfully!")