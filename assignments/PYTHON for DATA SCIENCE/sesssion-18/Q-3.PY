#Task 3: Fetch a list of users from https://jsonplaceholder.typicode.com/users using requests.get(), then use the .json() method to extract and print the usernames of all users whose email ends with '.org'


import requests

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
users = response.json()

print("Usernames with email ending in '.org':")
for user in users:
    if user.get('email', '').endswith('.org'):
        print("-", user['username'])