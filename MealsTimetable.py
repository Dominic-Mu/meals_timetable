import calendar
import random
import pandas as pd
from flask import Flask, render_template, request
random.seed(123)

app = Flask(__name__)

def generate_meal_combinations(meals):
    # Shuffling the meals to randomize the combinations
    random.shuffle(meals)

    return meals

def create_monthly_timetable(year, month, meals):
    # Getting the number of days in the given month
    _, last_day = calendar.monthrange(year, month)

    # Generating meal combinations for the month
    meal_combinations = generate_meal_combinations(meals)

    # Creating a timetable dictionary for each day of the month
    timetable = {}
    for day in range(1, last_day + 1):
        # Using modulus to loop through the meal combinations
        meal_index = (day - 1) % len(meal_combinations)
        timetable[f"{year}-{month:02d}-{day:02d}"] = meal_combinations[meal_index]

    return timetable

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Reading meals from Excel file
        meals_df = pd.read_excel('meals.xlsx')
        meals_column = meals_df['Meals'].tolist()

        # Getting user input for month and year
        selected_month = int(request.form['month'])
        selected_year = int(request.form['year'])

        # Generating timetable for the selected month and year
        timetable = create_monthly_timetable(selected_year, selected_month, meals_column)

        return render_template('index.html', timetable=timetable)

    return render_template('form.html')

if __name__ == "__main__":
    app.run(debug=True)
