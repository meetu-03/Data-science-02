#Task 1: Use the requests.get() function to fetch the latest posts from the JSONPlaceholder API endpoint https://jsonplaceholder.typicode.com/posts and print the status code and the first post's title.


import requests

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

print("Status Code:", response.status_code)

posts = response.json()
if posts:
    print("First Post Title:", posts[0]['title'])