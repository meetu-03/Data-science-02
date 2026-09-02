#2. Build a Python script that lets a user enter a new playlist name and description, sends this data as JSON in a POST request to a mock API endpoint (such as https://jsonplaceholder.typicode.com/posts), and prints the playlist ID returned by the API.



import requests

url = "https://jsonplaceholder.typicode.com/posts"
playlist_name = input("Enter playlist name: ")
playlist_desc = input("Enter playlist description: ")

payload = {
    "name": playlist_name,
    "description": playlist_desc
}

response = requests.post(url, json=payload)
data = response.json()
print(f"Returned Playlist ID: {data.get('id')}")