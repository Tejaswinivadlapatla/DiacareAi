def calculate_bmi(height_cm, weight_kg):
    """
    Calculate BMI and return:
    bmi value,
    category,
    advice
    """

    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)

    bmi = round(bmi, 1)

    if bmi < 18.5:
        category = "Underweight"
        advice = (
            "• Increase nutritious calorie intake.\n"
            "• Eat protein-rich foods.\n"
            "• Consult a dietitian if needed."
        )

    elif bmi < 25:
        category = "Normal Weight"
        advice = (
            "• Great! Maintain your healthy lifestyle.\n"
            "• Exercise regularly.\n"
            "• Eat a balanced diet."
        )

    elif bmi < 30:
        category = "Overweight"
        advice = (
            "• Reduce sugary foods.\n"
            "• Walk at least 30 minutes daily.\n"
            "• Increase fruits and vegetables."
        )

    else:
        category = "Obese"
        advice = (
            "• Follow a healthy meal plan.\n"
            "• Exercise under medical guidance.\n"
            "• Consult a healthcare professional."
        )

    return bmi, category, advice