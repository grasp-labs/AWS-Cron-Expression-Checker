import re

#Base 6‑Field Regex
aws_cron_regex = re.compile(
    r"^" +
    r"(?P<minutes>[^\s]+)\s+" +       # minutes
    r"(?P<hours>[^\s]+)\s+" +         # hours
    r"(?P<day_of_month>[^\s]+)\s+" +  # day-of-month
    r"(?P<month>[^\s]+)\s+" +         # month
    r"(?P<day_of_week>[^\s]+)\s+" +   # day-of-week
    r"(?P<year>[^\s]+)" +             # year
    r"$"
)

# Minute: 0-59
aws_minute_regex = re.compile(
    r"^(\*|\*/[1-9]\d*|([0]?[0-9]|[1-5]?[0-9])(-([0]?[0-9]|[1-5]?[0-9]))?(\/[1-9]\d*)?"
    r"(,([0]?[0-9]|[1-5]?[0-9])(-([0]?[0-9]|[1-5]?[0-9]))?(\/[1-9]\d*)?)*)$"
)

# Hour: 0-23
aws_hour_regex = re.compile(
    r"^(\*|\*/([1-9]|1\d|2[0-3])|(0|[1-9]|1\d|2[0-3])(-([1-9]|1\d|2[0-3]))?(\/([1-9]|1\d|2[0-3]))?(,(0|[1-9]|1\d|2[0-3])(-([1-9]|1\d|2[0-3]))?(\/([1-9]|1\d|2[0-3]))?)*)$"
)

# Day of month: 1-31, ?, L, W
aws_day_of_month_regex = re.compile(
    r"^(\*|\?|L|([1-9]|[12]\d|3[01])W?|([1-9]|[12]\d|3[01])(-([1-9]|[12]\d|3[01]))?(\/([1-9]\d*))?(,([1-9]|[12]\d|3[01])(-([1-9]|[12]\d|3[01]))?(\/([1-9]\d*))?)*)$"
)

# Month: 1-12 or JAN-DEC
aws_month_regex = re.compile(
    r"^(\*|\*/([1-9]|1[0-2])|([1-9]|1[0-2]|JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)(-([1-9]|1[0-2]|JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC))?(\/([1-9]|1[0-2]))?(,([1-9]|1[0-2]|JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)(-([1-9]|1[0-2]|JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC))?(\/([1-9]|1[0-2]))?)*)$"
)

# Day of week: 1-7 or SUN-SAT, ?, L, #
aws_day_of_week_regex = re.compile(
    r"^(\*|\?|L|([1-7]|SUN|MON|TUE|WED|THU|FRI|SAT)(L|#[1-5])?|([1-7]|SUN|MON|TUE|WED|THU|FRI|SAT)(-([1-7]|SUN|MON|TUE|WED|THU|FRI|SAT))?(\/[1-7])?(,([1-7]|SUN|MON|TUE|WED|THU|FRI|SAT)(L|#[1-5])?(-([1-7]|SUN|MON|TUE|WED|THU|FRI|SAT))?(\/[1-7])?)*)$"
)

# Year: 1970-2199 (AWS supports 1970-2199)
aws_year_regex = re.compile(
    r"^(\*|\*/(19[7-9]\d|20\d{2}|21\d{2})|((19[7-9]\d|20\d{2}|21\d{2])-(19[7-9]\d|20\d{2}|21\d{2}))?(\/[1-9]\d*)?(,(19[7-9]\d|20\d{2}|21\d{2])-(19[7-9]\d|20\d{2}|21\d{2])?(\/[1-9]\d*)?)*)$"
)