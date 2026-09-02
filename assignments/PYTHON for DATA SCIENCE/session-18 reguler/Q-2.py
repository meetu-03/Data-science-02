#ask 2: Write a Python function using re.search() that checks if a string contains a valid date in the format 'DD/MM/YYYY'. The function should return True if a date is found, otherwise False.

import re

def contains_valid_date(text):
    pattern = r'\b\d{2}/\d{2}/\d{4}\b'
    match = re.search(pattern, text)
    return bool(match)

# Test examples
print(contains_valid_date("The event is on 15/08/2026."))  # Returns True
print(contains_valid_date("No date mentioned here."))       # Returns False