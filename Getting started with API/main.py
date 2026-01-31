import requests
def generate_joke():
    print("Welcome to random joke generator")
    while True:
        print("Press 'enter' to genrate a new joke and to quit press 'q'.")
        choice = input()
        if choice == 'q':
            break
        else :
            URL = "https://official-joke-api.appspot.com/random_joke"
            response = requests.get(URL)
            if response.status_code == 200:
                joke_data = response.json()
                print("Ok let's start the joke :",joke_data['setup'])
                print("The punchline is:",joke_data['punchline'])

if __name__ == "__main__":
    generate_joke()