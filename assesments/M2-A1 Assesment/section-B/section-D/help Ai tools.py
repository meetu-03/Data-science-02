'''
# Use an AI tool of your choice (ChatGPT, Claude, GitHub Copilot, etc.) to help you write a Python
program for a food delivery platform that:
Fetches the first 5 records from https://jsonplaceholder.typicode.com/posts?_limit=5 (treating
them as restaurant records) and prints each restaurant's id and title.
Applies a tiered commission — 10% for orders up to Rs 200, 15% for Rs 201–Rs 500, and 20%
above Rs 500 — to a hardcoded list of 6 order amounts using map() and a lambda, and prints
each original amount alongside its calculated commission.
Handles an API failure (any status code other than 200) by printing a descriptive error
message and stopping execution — without raising an unhandled exception that crashes the
script.
Saves the 5 fetched restaurant records to a file called data/processed/restaurants.json using
json.dump() inside a with open() context manager, with an indent of 2 for readability.import requests
import json
import os

'''

# ANSWER...


# Function to calculate commission
def calculate_commission(amount):
    if amount <= 200:
        return amount * 0.10
    elif amount <= 500:
        return amount * 0.15
    else:
        return amount * 0.20


# Fetch restaurant records
url = "https://jsonplaceholder.typicode.com/posts?_limit=5"

response = requests.get(url)

# Handle API failure
if response.status_code != 200:
    print("API Error: Unable to fetch restaurant records.")
else:
    restaurants = response.json()

    # Print restaurant ID and title
    print("--- Restaurant Records ---")
    for restaurant in restaurants:
        print("ID:", restaurant["id"])
        print("Title:", restaurant["title"])
        print()

    # Order amounts
    orders = [150, 200, 250, 400, 600, 800]

    # Calculate commissions using map() and lambda
    commissions = list(
        map(lambda amount: calculate_commission(amount), orders)
    )

    # Print order amount and commission
    print("--- Order Commissions ---")
    for amount, commission in zip(orders, commissions):
        print(f"Order: Rs {amount} | Commission: Rs {commission:.2f}")

    # Save restaurant records
    os.makedirs("data/processed", exist_ok=True)

    with open("data/processed/restaurants.json", "w") as file:
        json.dump(restaurants, file, indent=2)

    print("\nRestaurant data saved successfully.")





