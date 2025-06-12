import re
import regexExpressions

def is_valid_field(expression: str, regex: re.Pattern[str]) -> bool:
    """
    Validates a field value using the provided regex pattern.

    Returns:
        bool: True if the expression fully matches the regex.
    """
    return bool(regex.fullmatch(expression))

def is_valid_cron_format(expression: str) -> bool:
    """
    Checks whether the given expression matches the AWS cron regex format.

    Args:
        expression: The cron expression to validate.

    Returns:
        True if the expression matches the AWS cron format, otherwise False.
    """
    return bool(regexExpressions.aws_cron_regex.fullmatch(expression))