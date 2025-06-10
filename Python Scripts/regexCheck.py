import re
import testCases

from text_utils import colorize_bool, colorize_question, colorize_regex
from regexExpressions import aws_minute_regex, original_minute_regex

def check_input_regex(regex_to_test: re.Pattern[str], test_cases) :
    # Evaluate each regex against test cases
    print(f"{'Input':<20} {'Expected':<8} {'Test'}")
    print("-" * 55)
    for value, expected in test_cases:
        provided_regex_result = bool(regex_to_test.fullmatch(value))
        print(
            f"{value:<20} "
            f"{colorize_bool(expected, 8)} "
            f"{colorize_bool(provided_regex_result, 0)} "
        )

def check_minutes():
    print("Checking minutes field...")
    check_input_regex(aws_minute_regex, testCases.minuteCases)

def check_hours():
    print("Checking hours field...")

def check_days():
    print("Checking days field...")

def check_months():
    print("Checking months field...")

def check_years():
    print("Checking years field...")

def check_full_cron():
    cron = input("Enter the full cron expression: ")
    print(f"You entered: {cron}")
    # Add validation logic here if needed

def main():
    print("What do you want to check?")
    print("1. Minutes")
    print("2. Hours")
    print("3. Days")
    print("4. Months")
    print("5. Years")
    print("6. Full cron expression")

    choice = input(f"{colorize_question('Choose an option (1-6): ')}").strip()

    match choice:
        case "1":
            check_minutes()
        case "2":
            check_hours()
        case "3":
            check_days()
        case "4":
            check_months()
        case "5":
            check_years()
        case "6":
            check_full_cron()
        case _:
            print("Invalid option. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()