#Task 4: Build a small script that fetches movies from the OMDB API (http://www.omdbapi.com/) by sending a GET request with query parameters: apikey='demo', s='Avengers'. Print the total number of results found. Hint: Pass the parameters using the params={} argument in requests.get().


import requests

url = "http://www.omdbapi.com/"
query_params = {
    "apikey": "demo",
    "s": "Avengers"
}

response = requests.get(url, params=query_params)
data = response.json()

if data.get("Response") == "True":
    print("Total Results Found:", data.get("totalResults"))
else:
    print("API Error:", data.get("Error"))