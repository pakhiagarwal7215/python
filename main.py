from config import hf_api_key
import requests
from colorama import Fore,Style,init

init(autoreset=True)

model= "google/pegasus-xsum"
base_url = "https://router.huggingface.co/hf-inference/models/"
api = base_url+model

header = {
    "Authorization": f"Bearer {hf_api_key}",
    "Content-Type": "application/json"
}

text = input("Enter the paragraph ;")
min_length = 30
max_length = 150
payload = {"inputs": text,"parameters":{"min_length":min_length,"max_length": max_length}}
print(Fore.BLUE + Style.BRIGHT + f"\n???? Performing AI summarization using model: {model}")
response = requests.post(api,headers=header,json=payload)

#print(Fore.GREEN+Style.BRIGHT+f"response code is :{response.status_code}")
if response.status_code == 200:
    result = response.json()
    print(Fore.GREEN + Style.BRIGHT +
          "\n✅ Summary:\n")
    print(result[0]["summary_text"])
else:
    print(Fore.RED + "\n❌ Error:")
    print(response.text)

