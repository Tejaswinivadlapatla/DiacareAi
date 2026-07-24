import random


def generate_meal_plan(diabetes_type, preference):

    veg_breakfast = [
        "Oats with Low-fat Milk + Apple",
        "Vegetable Upma + Orange",
        "Poha + Sprouts",
        "Idli with Sambar",
        "Vegetable Sandwich"
    ]

    veg_lunch = [
        "Brown Rice + Dal + Vegetable Curry + Salad",
        "Chapati + Mixed Vegetable Curry",
        "Millet Rice + Sambar + Beans",
        "Vegetable Pulao + Curd",
        "Quinoa + Paneer Curry"
    ]

    veg_snack = [
        "Green Tea + Almonds",
        "Roasted Chickpeas",
        "Fruit Salad",
        "Walnuts + Buttermilk",
        "Sprouts Salad"
    ]

    veg_dinner = [
        "Chapati + Paneer Curry",
        "Vegetable Soup + Salad",
        "Moong Dal Khichdi",
        "Roti + Palak Curry",
        "Vegetable Daliya"
    ]

    nonveg_breakfast = [
        "Boiled Eggs + Oats",
        "Egg Sandwich",
        "Omelette + Whole Wheat Bread",
        "Milk + Apple + Egg",
        "Boiled Eggs + Banana"
    ]

    nonveg_lunch = [
        "Brown Rice + Grilled Chicken + Salad",
        "Chapati + Fish Curry",
        "Chicken Curry + Millet Rice",
        "Egg Curry + Brown Rice",
        "Grilled Fish + Vegetables"
    ]

    nonveg_snack = [
        "Boiled Egg + Green Tea",
        "Almonds + Milk",
        "Fruit Salad",
        "Greek Yogurt",
        "Roasted Peanuts"
    ]

    nonveg_dinner = [
        "Grilled Chicken + Soup",
        "Fish + Vegetables",
        "Chapati + Egg Curry",
        "Chicken Salad",
        "Paneer + Boiled Egg"
    ]

    if preference == "Vegetarian":

        breakfast = random.choice(veg_breakfast)
        lunch = random.choice(veg_lunch)
        snack = random.choice(veg_snack)
        dinner = random.choice(veg_dinner)

    else:

        breakfast = random.choice(nonveg_breakfast)
        lunch = random.choice(nonveg_lunch)
        snack = random.choice(nonveg_snack)
        dinner = random.choice(nonveg_dinner)

    if diabetes_type == "Prediabetes":

        water = "2.5 Litres"
        tip = "Avoid sugary drinks and walk for 30 minutes daily."

    elif diabetes_type == "Type 1":

        water = "3 Litres"
        tip = "Monitor blood sugar before meals and never skip insulin."

    else:

        water = "3 Litres"
        tip = "Choose high-fiber foods and avoid refined sugar."

    return {

        "Breakfast": breakfast,
        "Lunch": lunch,
        "Snack": snack,
        "Dinner": dinner,
        "Water": water,
        "Tip": tip

    }