from services.nutrition_service import get_nutrition

food = input("Enter Food Name: ")

result = get_nutrition(food)

if result:
    print("\nNutrition Information\n")

    for key, value in result.items():
        print(f"{key}: {value}")

else:
    print("Food not found.")