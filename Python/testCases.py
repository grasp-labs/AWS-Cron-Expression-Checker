import os
import json

# Open and load the JSON file
minute_cases_path = os.path.join(os.path.dirname(__file__), '..', 'testCases', 'minuteCases.json')
with open('../testCases/minuteCases.json', 'r') as file:
    minute_cases = json.load(file)

hour_cases_path = os.path.join(os.path.dirname(__file__), '..', 'testCases', 'hourCases.json')
with open('../testCases/hourCases.json', 'r') as file:
    hour_cases = json.load(file)

day_of_week_cases_path = os.path.join(os.path.dirname(__file__), '..', 'testCases', 'dayOfWeekCases.json')
with open('../testCases/dayOfWeekCases.json', 'r') as file:
    day_of_week_cases = json.load(file)

day_of_month_cases_path = os.path.join(os.path.dirname(__file__), '..', 'testCases', 'dayOfMonthCases.json')
with open('../testCases/dayOfMonthCases.json', 'r') as file:
    day_of_month_cases = json.load(file)

month_cases_path = os.path.join(os.path.dirname(__file__), '..', 'testCases', 'monthCases.json')
with open('../testCases/monthCases.json', 'r') as file:
    month_cases = json.load(file)

year_cases_path = os.path.join(os.path.dirname(__file__), '..', 'testCases', 'yearCases.json')
with open('../testCases/yearCases.json', 'r') as file:
    year_cases = json.load(file)