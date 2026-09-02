#Task 1: Use re.findall() to extract all valid phone numbers from a given string in the format '+91-XXXXXXXXXX' (e.g., '+91-9876543210'). Print the list of found numbers.

import re

text = "Call me at +91-9876543210 or +91-1234567890. Invalid numbers: 9876543210, +91-123."
pattern = r'\+91-\d{10}'

phone_numbers = re.findall(pattern, text)
print("Found phone numbers:", phone_numbers)