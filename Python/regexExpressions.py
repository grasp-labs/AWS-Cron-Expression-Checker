import re

#Base 6‑Field Regex
aws_cron_regex = re.compile(
    r"^" +
    r"(?P<minutes>\S+)\s+" +       # minutes
    r"(?P<hours>\S+)\s+" +         # hours
    r"(?P<day_of_month>\S+)\s+" +  # day-of-month
    r"(?P<month>\S+)\s+" +         # month
    r"(?P<day_of_week>\S+)\s+" +   # day-of-week
    r"(?P<year>\S+)" +             # year
    r"$"
)

# AWS Minute field regex:
# Matches valid AWS cron expressions for the minute field.
# Allows:
# - "*" to indicate every minute
# - "*/n" for step values, meaning every n minutes (n must be a positive integer)
# - Single minute values between 0 and 59 (optional leading zero allowed)
# - Ranges like "10-20", inclusive
# - Step values following a single value or range (e.g., "5/15" or "10-30/5")
# - Multiple comma-separated values combining any of the above formats
# Disallows:
# - Values outside 0–59
# - Leading "*" combined with step value and other values (e.g., "*/5,10")
# - Empty segments or trailing/leading commas
aws_minute_regex = re.compile(
    r"^(\*|\*/[1-9]\d*|(0?[0-9]|[1-5]?[0-9])(-(0?[0-9]|[1-5]?[0-9]))?(/[1-9]\d*)?(,(0?[0-9]|[1-5]?[0-9])(-(0?[0-9]|[1-5]?[0-9]))?(/[1-9]\d*)?)*)$"
)

# AWS Hour field regex:
# Matches valid AWS cron expressions for the hour field.
# Allows:
# - "*" (every hour)
# - "*/n" step values (every n hours, where 1 ≤ n ≤ 23)
# - Single hour values (0–23)
# - Ranges (e.g., "5-10"), inclusive
# - Step values after a single value or range (e.g., "3/4" or "5-10/2")
# - Multiple values separated by commas combining any of the above
# Disallows:
# - Values outside 0–23
# - Steps or ranges with invalid numbers (e.g., "25", "0-30", "*/0")
aws_hour_regex = re.compile(
    r"^(\*|\*/([1-9]|1[0-9]|2[0-3])|(0|[1-9]|1[0-9]|2[0-3])(-([0-9]|1[0-9]|2[0-3]))?(/([1-9]|1[0-9]|2[0-3]))?(,(0|[1-9]|1[0-9]|2[0-3])(-([0-9]|1[0-9]|2[0-3]))?(/([1-9]|1[0-9]|2[0-3]))?)*)$"
)

# AWS Day of Month regex for cron expressions:
# Supports:
# - "*" (every day of the month)
# - "?" (no specific value — used when this field is not specified)
# - "L" (the last day of the month)
# - Specific days: 1 through 31
# - "W" modifier: Nearest weekday to a given day (e.g., "15W")
# - Ranges (e.g., "5-10") with optional step values (e.g., "5-20/3")
# - Multiple values separated by commas (e.g., "1,15,20W,25-30/2")
#
# Rules:
# - Valid day values are from 1 to 31
# - "W" can only follow a single day (e.g., "10W"), not a range or list
# - Steps ("/n") must be positive integers (1 or higher)
# - "L" cannot be combined with other values or modifiers
# - Comma-separated values must each be valid expressions
# - No support for "#" or "L" in combinations
#
# Examples of valid expressions:
#   "*"
#   "?"
#   "L"
#   "15"
#   "10W"
#   "5-20"
#   "1-30/2"
#   "1,15,25-30/2"
#   "15W,20"
#
# Examples of invalid expressions:
#   "0"             # day starts at 1
#   "32"            # day ends at 31
#   "1-32"          # range exceeds max day
#   "L,15"          # L cannot be part of a list
#   "15/L"          # step not allowed after a single day with W
#   "15W-20"        # W not allowed in a range
#   "15W/2"         # step not allowed with W
#   ",15"           # leading comma
#   "15,"           # trailing comma
aws_day_of_month_regex = re.compile(
    r"^(\*|\?|L|(\*/[1-9]\d*)|([1-9]|[12]\d|3[01])W?|([1-9]|[12]\d|3[01])(-([1-9]|[12]\d|3[01]))?(/([1-9]\d*))?(,([1-9]|[12]\d|3[01])(-([1-9]|[12]\d|3[01]))?(/([1-9]\d*))?)*)$")

# AWS Month regex matches:
# Month field regex for cron-like expressions:
# Allows two exclusive modes (no mixing names and numbers in the same expression):
#
# 1) Numeric mode:
#    - "*" (every month)
#    - "*/n" (every n months, where n is 1 to 12)
#    - Single month numbers (1-12)
#    - Ranges of months by number (e.g., "1-6", "12-1" for reverse ranges)
#    - Steps after a single number or range (e.g., "5/2", "1-10/3")
#    - Multiple values separated by commas combining any of the above (e.g., "1,6,12", "1-6,8-12")
#
# 2) Name mode:
#    - "*" (every month)
#    - "*/n" (every n months, where n is 1 to 12; steps still numeric)
#    - Single month names (JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC)
#    - Ranges of months by name (e.g., "JAN-MAR", "DEC-JAN" for reverse ranges)
#    - Steps after a single name or range (e.g., "JAN/3", "FEB-SEP/2")
#    - Multiple values separated by commas combining any of the above (e.g., "JAN,JUN,DEC", "MAR-MAY,JUL-SEP")
#
# Restrictions:
# - Mixing of numeric and named months in the same expression is not allowed
# - Numeric values are only allowed in the range 1-12 (no zero-padding)
# - No spaces allowed in the expression
# - No special characters except "*", "/", "-", and ","
#
# Examples of valid expressions:
# - "*"
# - "1"
# - "JAN"
# - "1-12"
# - "JAN-DEC"
# - "1,6,12"
# - "JAN,JUN,DEC"
# - "*/3"
# - "5-10/2"
# - "FEB/3"
# - "12-1" (reverse range)
#
# Examples of invalid expressions:
# - "JAN-12"  (mixed range of name and number)
# - "1,JUN"   (mixed list of number and name)
# - "0"       (zero is invalid month)
# - "13"      (above 12)
# - "05-10"   (zero-padded numbers not allowed)
# - "JAN,FOO" (invalid month name)
# - " 1-10 "  (spaces not allowed)
# - "5,,10"   (empty list element)
# - "5/2/3"   (multiple steps not allowed)
aws_month_regex = re.compile(
    r"^((\*|\*/([1-9]|1[0-2])|([1-9]|1[0-2])(-([1-9]|1[0-2]))?(/([1-9]|1[0-2]))?(,([1-9]|1[0-2])(-([1-9]|1[0-2]))?(/([1-9]|1[0-2]))?)*)|(\*|\*/([1-9]|1[0-2])|(JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)(-(JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC))?(/([1-9]|1[0-2]))?(,(JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)(-(JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC))?(/([1-9]|1[0-2]))?)*) )$"
)

# AWS Day of Week regex for cron expressions:
# Supports:
# - "*" (any day)
# - "?" (no specific value)
# - "L" (last specific weekday in month)
# - Days as numbers 1-7 (Sunday=1) or names SUN, MON, TUE, WED, THU, FRI, SAT
# - Modifiers:
#    * "L" appended to day (e.g., "5L" for last Thursday)
#    * "#" followed by 1-5 (e.g., "FRI#3" means 3rd Friday of month)
# - Ranges (e.g., "MON-FRI", "1-5"), including reverse ranges like "7-1"
# - Steps (e.g., "5/2" means every 2 days starting at day 5)
# - Multiple values separated by commas (e.g., "MON,WED,FRI", "1,3,5")
#
# Restrictions and notes:
# - Days are only 1-7 (no zero or >7)
# - Names must be valid day abbreviations only (SUN-SAT)
# - No spaces allowed anywhere in the expression
# - "*" cannot be used with steps (e.g., "*/4" invalid)
# - Only one modifier (# or L) allowed per day element
# - Multiple slashes or empty list elements not allowed
# - Duplicate days allowed, but no invalid values
# - Expression must not start or end with commas
# - Examples of valid expressions:
#    "*"
#    "?"
#    "L"
#    "1"
#    "SUN"
#    "MON-FRI"
#    "7-1"
#    "5/2"
#    "MON,WED,FRI"
#    "FRI#3"
#    "5L"
#
# Examples of invalid expressions:
#    "0"         # zero day invalid
#    "8"         # >7 invalid
#    "*/4"       # step with leading *
#    "1,8"       # invalid day in list
#    "MON,FOO"   # invalid day name
#    "5,,7"      # empty list element
#    ",5,7"      # leading comma
#    "5,7,"      # trailing comma
#    "5/2/3"     # multiple slashes
#    "5.5"       # decimal not allowed
#    "5#6"       # invalid # occurrence (>5)
#    "FRI#0"     # invalid # occurrence (0)
#    "8L"        # invalid day with L
#    ""          # empty string not allowed
aws_day_of_week_regex = re.compile(
    r"^(\*|\?|L|([1-7]|SUN|MON|TUE|WED|THU|FRI|SAT)(L|#[1-5])?|([1-7]|SUN|MON|TUE|WED|THU|FRI|SAT)(-([1-7]|SUN|MON|TUE|WED|THU|FRI|SAT))?(/[1-7])?(,([1-7]|SUN|MON|TUE|WED|THU|FRI|SAT)(L|#[1-5])?(-([1-7]|SUN|MON|TUE|WED|THU|FRI|SAT))?(/[1-7])?)*)$"
)

# AWS Year field regex:
# Matches valid AWS cron expressions for the "year" field.
# Allows:
# - "*" to indicate every year
# - "*/n" for step values starting from the beginning of the allowed range (e.g., "*/5")
# - Specific 4-digit years from 1970 to 2199
# - Year ranges (e.g., "2020-2030"), inclusive
# - Optional step values following a specific year or range (e.g., "2020/5" or "2020-2030/2")
# - Comma-separated lists of any valid year expression
# Disallows:
# - Years before 1970 or after 2199
# - Invalid ranges (e.g., 2030-2020)
# - Invalid step values (e.g., "/0", "/-5")
# - Leading/trailing commas, or empty segments
aws_year_regex = re.compile(
    r"^(\*|(\*/[1-9]\d*)|((19[7-9]\d|20\d{2}|21\d{2})(-(19[7-9]\d|20\d{2}|21\d{2}))?(/[1-9]\d*)?)(,((19[7-9]\d|20\d{2}|21\d{2})(-(19[7-9]\d|20\d{2}|21\d{2}))?(/[1-9]\d*)?))*)$"
)