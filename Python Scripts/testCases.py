import re

# Test cases: format (test_string, is_valid_aws)
minuteCases = [
    ("*", True), # All minutes
    ("0", True), # At minute 0
    ("59", True), # At minute 59
    ("60", False), # At minute 60 not allowed
    ("5-10", True), # Between minute 5 and 10
    ("55-5", True), # AWS allows reverse ranges, executes in order. 55-5 executes at minutes 55 though 59 of the hour
    # and wraps to the next hour for the remaining 5 minutes. (55,56,57,58,59,00,01,02,03,04,05).
    ("60/15", False), # Minute 60 not allowed
    ("0/15", True), # Every 15 minutes
    ("*/5", True), # Every 5 minutes starting at 0 through 55 (5,10,15,...,50,55)
    ("5/0", False), # Every 0 minutes not allowed
    ("0,15,30,45", True), # List of minutes
    ("0,15,30,60", False), # List of minutes, 60 not allowed
    ("0,15,61", False), # List of minutes, 60+ not allowed
    ("5-10,20,30-40/5", True), # Mixed true case
    ("5,10/2", True), # Mixed true case
    ("5,10-15", True), # Mixed true case
    (",5", False), # Trailing commas not allowed
    ("", False), # Empty string not allowed
    ("5,", False), # Empty value after comma not allowed
    ("05", False),  # AWS does not allow padded values
    ("005", False),  # AWS does not allow padded values away from one zero
]
