from services.prediction_service import predict_diabetes

result, confidence = predict_diabetes(
    pregnancies=2,
    glucose=120,
    blood_pressure=70,
    skin_thickness=20,
    insulin=85,
    bmi=28.5,
    dpf=0.35,
    age=30
)

print("Prediction :", result)
print("Confidence :", confidence, "%")