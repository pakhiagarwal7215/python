import requests

# Example of facing a random joke

url = "https://official-joke-api.appspot.com/random_joke"

# Send GET request to fetch a joke

response = requests.get(url)

if response.status_code == 200:

    joke_data = response.json()

    print(f"Joke : {joke_data['setup']} - {joke_data['punchline']}")

else:
    
    print(f"Failed to retrive joke.Status code: {response.status_code}")