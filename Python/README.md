# AWS Cron Expression Checker (Python)

A Python utility for validating AWS cron expressions, including detailed field-by-field validation and helpful error messages.

---

## Features

- **Validate full AWS cron expressions**  
- **Field-by-field validation** (minutes, hours, day-of-month, month, day-of-week, year)
- **Detailed error reporting** (explains which field is invalid and why)
- **Comprehensive test cases** for all fields
- **Easy to use as a function or console app**

---

## Installation

**Function Only:**
- Copy `regexExpressions.py` into your project.

**Console App:**
- Copy the entire `Python` folder and the `testCases` folder into your project.

---

## Usage

### Validate a Full Cron Expression (Function Only)

```python
import regexExpressions

def validate_full_cron(expression: str):
    match = regexExpressions.aws_cron_regex.fullmatch(expression)
    print(bool(match))

if __name__ == "__main__":
    validate_full_cron("5 * * * * *")
```
Returns `True` if the input string is a valid AWS cron expression, otherwise `False`.

---

### Validate Each Field

You can use the regex patterns in `regexExpressions.py` to validate individual fields (minutes, hours, etc.).

---

### Console App

Run the console app for interactive validation and test case checking:

```python
from regex_console_app import main

if __name__ == "__main__":
    main()
```

Or, for field-by-field validation:

```python
from regexCheck import is_valid_field
import regexExpressions

print(is_valid_field("5", regexExpressions.aws_minute_regex))  # True
print(is_valid_field("60", regexExpressions.aws_minute_regex)) # False
```

---

## AWS Cron Expression Format

AWS cron expressions use the following format:

```
Minutes Hours Day-of-month Month Day-of-week Year
```

Refer to the [AWS documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html#CronExpressions) for more details.

---

## Test Cases

Comprehensive test cases for each field are provided in the `testCases` folder.

---

## License

MIT License