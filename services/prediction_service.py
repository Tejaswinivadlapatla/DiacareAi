import pickle
import numpy as np

# ==============================
# Load Model
# ==============================

with open("models/diabetes_model.pkl", "rb") as f:
    model = pickle.load(f)

# ==============================
# Load Scaler
# ==============================

with open("models/scaler_model.pkl", "rb") as f:
    scaler = pickle.load(f)


# ==============================
# Predict Function
# ==============================

def predict_diabetes(
    pregnancies,
    glucose,
    blood_pressure,
    skin_thickness,
    insulin,
    bmi,
    dpf,
    age
):

    data = np.array([[
        pregnancies,
        glucose,
        blood_pressure,
        skin_thickness,
        insulin,
        bmi,
        dpf,
        age
    ]])

    # Scale the input
    data = scaler.transform(data)

    # Prediction
    prediction = model.predict(data)[0]

    # Probability
    probability = model.predict_proba(data)[0]

    confidence = round(max(probability) * 100, 2)

    if prediction == 1:
        result = "Diabetic"
    else:
        result = "Non-Diabetic"

    return result, confidence