BMI Calculator + Health Assistant (Python Project)
 Project Overview
This Python project is designed for first-semester B.Tech students to practice basic Python programming, functions, conditional statements, loops, and use of standard modules such as math and datetime.
The program calculates the Body Mass Index (BMI) of a user based on their height and weight, categorizes their BMI, and provides personalized health tips. It also calculates recommended daily water intake and displays the current date and time.

 Features

Calculate BMI using weight and height

Categorize BMI into:

Underweight

Normal Weight

Overweight

Obesity

Provide personalized health tips based on BMI category

Suggest daily water intake using the “33 ml per kg” rule

Display current date and time using datetime module

User-friendly and beginner-friendly code structure


Modules Used

math – for mathematical operations

datetime – for displaying current time and date


 How the Program Works

User enters:

Name

Age

Weight (kg)

Height (meters)

Program calculates BMI:

BMI = weight / (height ** 2)


Based on BMI, it assigns a health category.

Program displays:

BMI

BMI Category

Recommended Health Tips

Daily Water Intake

Report Generation Date & Time


 Code Structure

The program is divided into functions for clarity:

calculate_bmi() – computes BMI

bmi_category() – returns BMI category

health_tips() – provides tips based on category

water_intake() – calculates water intake

show_current_time() – prints current time


How to Run the Project

Install Python 3.x

Save the program as bmi_health_assistant.py

Open terminal or command prompt

Run the script:

python bmi_health_assistant.py


 Sample Output
BMI CALCULATOR + HEALTH ASSISTANT
Enter your name: John
Enter your age: 20
Enter your weight in kg: 65
Enter your height in meters: 1.72

Hello John, Age: 20
Your BMI is: 21.97
Category: Normal Weight

--- Health Tips for You ---
- Maintain a balanced diet.
- Exercise 4–5 times a week.
- Drink plenty of water daily.

Recommended Water Intake: 2.15 liters/day
Health Report Generated On: 23-11-2025 06:30:20 PM

Stay healthy! Take care :)


 Educational Purpose

This project helps students learn:

Functions

Conditionals (if-elif-else)

Input/Output operations

Using modules (math, datetime)

Clean coding practices# BMI-AND-HEALTH
