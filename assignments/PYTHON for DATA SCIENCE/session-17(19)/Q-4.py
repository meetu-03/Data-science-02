#Task 4: Modify your GET request to https://jsonplaceholder.typicode.com/posts so it only fetches posts by userId=2 by passing the correct query parameter. Print the IDs of the returned posts. Hint: Use the 'params' argument in requests.get().


import requests

url = "https://jsonplaceholder.typicode.com/posts"
query_params = {"userId": 2}

response = requests.get(url, params=query_params)
posts = response.json()

post_ids = [post['id'] for post in posts]
print("Post IDs for userId=2:", post_ids)