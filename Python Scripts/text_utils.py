class Style:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

def colorize_bool(result: bool, width: int) -> str:
    """
    Returns the string formatted with the appropriate color based on validity.

    Args:
        result (bool): Was the test result true or false.
        width (int): The fixed width for formatting.

    Returns:
        str: The color-formatted string.
    """
    color = Style.RESET if result == True else Style.RED
    return f"{color}{str(result):<{width}}{Style.RESET}"

def colorize_question(val) -> str:
    """
    Returns the string formatted with the appropriate color.

    Args:
        val (str): String to colorize.

    Returns:
        str: The color-formatted string.
    """
    return f"{Style.GREEN}{val}{Style.RESET}"

def colorize_regex(val) -> str:
    """
    Returns the string formatted with the appropriate color.

    Args:
        val (str): String to colorize.

    Returns:
        str: The color-formatted string.
    """
    return f"{Style.YELLOW}{val}{Style.RESET}"
