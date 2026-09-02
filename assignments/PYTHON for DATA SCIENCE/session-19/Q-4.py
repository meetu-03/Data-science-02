#4. Write a script that fetches the latest 5 posts from https://jsonplaceholder.typicode.com/posts, parses the JSON response, and saves the post titles and userIds to a CSV file called posts.csv.(Hint: Use the csv module for writing to CSV.)


import requests
import csv

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
# Fetching the first 5 posts using list slicing
posts = response.json()[:5] 

with open('posts.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'User ID']) # Header row
    for post in posts:
        writer.writerow([post['title'], post['userId']])
        
print("Successfully saved to posts.csv")