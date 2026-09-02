#5. Modify your script to save the same API data (latest 5 posts from https://jsonplaceholder.typicode.com/posts) into a JSON file named posts.json instead of CSV.



import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
posts = response.json()[:5]

# Filtering to keep only the required data (Title and User ID)
filtered_data = [{"title": post["title"], "userId": post["userId"]} for post in posts]

with open('posts.json', 'w', encoding='utf-8') as file:
    json.dump(filtered_data, file, indent=4)
    
print("Successfully saved to posts.json")