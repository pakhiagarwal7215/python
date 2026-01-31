import requests
def random_joke():
    URL = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(URL)
    print(response.status_code)
    if response.status_code == 200:
        data = response.json()
        print(data['setup'])
        print(data['punchline'])
random_joke()