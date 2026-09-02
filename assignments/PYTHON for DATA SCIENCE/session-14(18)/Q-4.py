#Task 4: Use re.sub() to replace all email addresses in a string with '[hidden email]' and print the modified string. Constraint: Do not use any external libraries except re.


import re

text = "Contact support at help@example.com or user.name123@domain.org for queries."
pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

masked_text = re.sub(pattern, '[hidden email]', text)
print("Modified string:")
print(masked_text)