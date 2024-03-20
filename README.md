# Meal Timetable Generator

A simple Flask web application to generate a monthly timetable for meals, allowing users to select the month and year.

## Features

- Dynamic generation of a monthly meal timetable.
- User-friendly web interface to select the desired month and year.
- Meal options read from an Excel file for easy customization.

## Prerequisites

Make sure you have the following installed:

- Python (3.6 or higher)
- pip
- Flask
- pandas

Install the required Python packages using the following command:

```bash
pip install flask pandas
```

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/Dominic-Mu/meals_timetable.git
cd meals_timetable
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python MealsTimetable.py
```

4. Open your web browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Usage

1. The home page presents a form where you can select the desired month and year.

2. After selecting the month and year, click the "Generate Timetable" button.

3. The generated monthly timetable will be displayed, showing the date and corresponding meal for each day.

## Customization

To customize the meal options, edit the `meals.xlsx` Excel file. Add or remove meals in the "Meals" column.

## Contributing

Feel free to contribute to the project by opening issues or submitting pull requests. Your feedback and contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the Flask and pandas communities for their excellent documentation and support.
