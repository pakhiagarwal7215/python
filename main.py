import requests

URL = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"
def generate_facts():
    while True:
        choice = input("press g to generate facts and press q to quit")
        if choice == 'g':
            response = requests.get(URL)
            if response.status_code == 200:
                data = response.json()
                print(data['text'])
        else:
            print("Goodbye")
if __name__ == "__main__":
    generate_facts()   
