#Task 3: Send a POST request to https://jsonplaceholder.typicode.com/posts to add a new post with fields: title, userId, and body. Print the status code and the JSON response. Hint: Use requests.post() and pass your data as a JSON payload.



import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "My New Post",
    "body": "This is the content of the post.",
    "userId": 1
}

response = requests.post(url, json=payload)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())