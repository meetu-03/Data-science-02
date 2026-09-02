# Task 5: Research using ChatGPT or Copilot to find out how to set custom HTTP headers (like 'Authorization') in a Python requests call. Write a short code snippet that sends a GET request to any API endpoint with a custom header and print the response status code.


import requests

url = "https://jsonplaceholder.typicode.com/posts"

# Set custom headers
custom_headers = {
    "Authorization": "Bearer fake_token_12345",
    "User-Agent": "MyCustomApp/1.0"
}

response = requests.get(url, headers=custom_headers)
print("Response Status Code:", response.status_code)