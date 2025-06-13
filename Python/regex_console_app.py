import re
import testCases
import regexExpressions
from regexCheck import is_valid_field

from text_utils import colorize_bool, colorize_question, description_color


def print_test_header():
    print(f"{'Input':<20} {'Expected':<8} {'Test':<8} Comment")
    print("-" * 60)


def run_regex_test(regex: re.Pattern[str], test_cases: list[dict]):
    """
    Tests a regex pattern against a set of test cases and prints the results.
    """
    print_test_header()
    for case in test_cases:
        expression = case.get("expression", "")
        expected_valid = case.get("valid", False)
        comment = case.get("comment", "")
        actual_valid = is_valid_field(expression, regex)

        print(
            f"{expression:<20} "
            f"{colorize_bool(expected_valid, 8)} "
            f"{colorize_bool(actual_valid, 8)} "
            f"{description_color('# ' + comment)}"
        )

def run_aws_cron_test(expression: str) -> tuple[bool, list[str]]:
    """
    Validates a full AWS cron expression against field-level regexes
    and AWS rules (e.g., one '?' in day-of-week or day-of-month).
    """
    errors = []
    match = regexExpressions.aws_cron_regex.fullmatch(expression)

    if not match:
        return False, ["Expression does not match AWS cron format."]

    fields = match.groupdict()

    validators = [
        ("minutes", regexExpressions.aws_minute_regex),
        ("hours", regexExpressions.aws_hour_regex),
        ("day_of_month", regexExpressions.aws_day_of_month_regex),
        ("month", regexExpressions.aws_month_regex),
        ("day_of_week", regexExpressions.aws_day_of_week_regex),
        ("year", regexExpressions.aws_year_regex),
    ]

    for field_name, regex in validators:
        if not regex.fullmatch(fields[field_name]):
            errors.append(f"{field_name.replace('_', ' ').title()} field '{fields[field_name]}' is invalid.")

    # AWS-specific rule: Only one '?' allowed in either day-of-month or day-of-week
    dom_has_q = '?' in fields["day_of_month"]
    dow_has_q = '?' in fields["day_of_week"]

    if dom_has_q and dow_has_q:
        errors.append("Both day-of-month and day-of-week fields cannot have '?'. Only one is allowed.")
    elif not dom_has_q and not dow_has_q:
        errors.append("Exactly one of day-of-month or day-of-week fields must have '?'.")

    return len(errors) == 0, errors


def prompt_and_validate_full_cron():
    """
    Prompts the user for a full AWS cron expression and validates it.
    """
    cron = input("Enter the full cron expression (min hr day(month) month day(week) year): ").strip()
    valid, errors = run_aws_cron_test(cron)
    print()

    if valid:
        print("✅ Valid AWS cron expression!")
    else:
        print("❌ Invalid AWS cron expression. Issues found:")
        for err in errors:
            print(f" - {err}")


def run_tests_for(field: str):
    """
    Maps a field name to its regex and test cases and runs the tests.
    """
    field_map = {
        "minutes": (regexExpressions.aws_minute_regex, testCases.minute_cases),
        "hours": (regexExpressions.aws_hour_regex, testCases.hour_cases),
        "day_of_month": (regexExpressions.aws_day_of_month_regex, testCases.day_of_month_cases),
        "day_of_week": (regexExpressions.aws_day_of_week_regex, testCases.day_of_week_cases),
        "month": (regexExpressions.aws_month_regex, testCases.month_cases),
        "year": (regexExpressions.aws_year_regex, testCases.year_cases),
    }

    if field in field_map:
        print(f"Checking {field.replace('_', ' ')} field...")
        regex, cases = field_map[field]
        run_regex_test(regex, cases)


def main():
    """
    Main menu loop to choose field-specific or full cron validation.
    """
    print("\nWhich Regex would you like to test against?")
    print("1. Minutes")
    print("2. Hours")
    print("3. Day of Month")
    print("4. Month")
    print("5. Day of Week")
    print("6. Year")
    print("7. Full AWS cron expression")

    choice = input(f"{colorize_question('Choose an option (1-6): ')}").strip()
    print()

    match choice:
        case "1": run_tests_for("minutes")
        case "2": run_tests_for("hours")
        case "3": run_tests_for("day_of_month")
        case "4": run_tests_for("month")
        case "5": run_tests_for("day_of_week")
        case "6": run_tests_for("year")
        case "7": prompt_and_validate_full_cron()
        case _: print("Invalid option. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
