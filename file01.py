import math
from datetime import datetime

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)


def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def health_tips(category):
    if category == "Underweight":
        return [
            "Increase calorie intake with nutritious foods.",
            "Add healthy fats like nuts, seeds, and avocados.",
            "Strength training helps gain muscle weight."
        ]
    elif category == "Normal Weight":
        return [
            "Maintain a balanced diet.",
            "Exercise 4–5 times a week.",
            "Drink plenty of water daily."
        ]
    elif category == "Overweight":
        return [
            "Reduce sugar and junk food.",
            "Walk 8,000–10,000 steps daily.",
            "Try portion control and healthy meals."
        ]
    else:
        return [
            "Consult a doctor for proper diet planning.",
            "Avoid oily and processed food.",
            "Start low-intensity exercises regularly."
        ]

def water_intake(weight):
    liters = weight * 0.033   # 33 ml per kg rule
    return round(liters, 2)


def show_current_time():
    now = datetime.now()
    return now.strftime("%d-%m-%Y %I:%M:%S %p")


print("      BMI CALCULATOR + HEALTH ASSISTANT")


name = input("Enter your name: ")
age = int(input("Enter your age: "))
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

print("Calculating your BMI... Please wait!")


# BMI calculation
bmi_value = calculate_bmi(weight, height)
category = bmi_category(bmi_value)

print(f"Hello {name}, Age: {age}")
print(f"Your BMI is: {bmi_value}")
print(f"Category: {category}")

# Health tips
print("\n--- Health Tips for You ---")
tips = health_tips(category)
for t in tips:
    print("- " + t)

# Water intake 
recommended_water = water_intake(weight)
print(f"\nRecommended Water Intake: {recommended_water} liters/day")

#date and time
print("\nHealth Report Generated On:", show_current_time())


print("      Stay healthy! Take care :)")

