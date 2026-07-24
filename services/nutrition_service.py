import pandas as pd
import os

# Path to the dataset
DATASET_PATH = os.path.join("database", "nutrition_dataset.csv")

# Load dataset only once
try:
    df = pd.read_csv(DATASET_PATH)

    # Remove unnecessary columns if present
    df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

    # Make searching easier
    df["food"] = df["food"].astype(str).str.strip().str.lower()

except Exception as e:
    print("Error loading nutrition dataset:", e)
    df = pd.DataFrame()


def get_nutrition(food_name):
    """
    Search for a food item and return its nutrition details.
    """

    food_name = food_name.strip().lower()

    result = df[df["food"] == food_name]

    if result.empty:
        return None

    food = result.iloc[0]

    return {
        "Food": food["food"].title(),
        "Calories": food["Caloric Value"],
        "Protein": food["Protein"],
        "Carbohydrates": food["Carbohydrates"],
        "Fat": food["Fat"],
        "Sugar": food["Sugars"],
        "Fiber": food["Dietary Fiber"],
        "Cholesterol": food["Cholesterol"],
        "Sodium": food["Sodium"]
    }