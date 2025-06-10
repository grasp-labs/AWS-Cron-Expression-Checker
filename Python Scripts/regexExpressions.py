import re

# Original minute regex (too permissive)
original_minute_regex = re.compile(
    r"^([*]|([0]?[0-5]?[0-9]?)|(([0]?[0-5]?[0-9]?)(\/|\-)([0]?[0-5]?[0-9]?))|"
    r"(([0]?[0-5]?[0-9]?)((\,)([0]?[0-5]?[0-9]?))*))$"
)
# Correct AWS cron minute field regex
aws_minute_regex = re.compile(
    r"^(\*|\*/[1-9]\d*|([0-5]?\d)(-[0-5]?\d)?(\/[1-9]\d*)?(,([0-5]?\d)(-[0-5]?\d)?(\/[1-9]\d*)?)*)$"
)