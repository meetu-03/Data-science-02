#Task 3: Given a block of text containing multiple prices (like 'Rs. 299', 'Rs. 1500', etc.), use re.findall() to extract all the numeric price values as integers and print their sum. Hint: Look for patterns like 'Rs. ' followed by one or more digits.


import re

text = "Item A costs Rs. 299, Item B costs Rs. 1500, and Item C is Rs. 450."
pattern = r'Rs\.\s*(\d+)'

# Extract digits and convert to integers
prices = [int(price) for price in re.findall(pattern, text)]
total_sum = sum(prices)

print("Extracted prices:", prices)
print("Sum of prices:", total_sum)