#Task 2: Create a Python dictionary that represents a Zomato-style restaurant object with fields like name, location, cuisines, and ratings. Convert this dictionary to a JSON string using the json module and print the result.


import json

restaurant = {
    "name": "The Spice Hub",
    "location": "Ahmedabad",
    "cuisines": ["North Indian", "Gujarati", "Chinese"],
    "rating": 4.5
}

# Convert dictionary to JSON string
json_data = json.dumps(restaurant, indent=4)
print(json_data)