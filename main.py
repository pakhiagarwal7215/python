from config import hf_api_key
import requests
from colorama import Fore,Style,init
from io import BytesIO
from PIL import Image
init(autoreset = True)

model = "stabilityai/stable-diffusion-xl-base-1.0"
base_url = "https://router.huggingface.co/hf-inference/models/"
API_url = base_url+model
headers = {"Authorization":f"Bearer {hf_api_key}"}

text = input("enter a prompt to create an image:")
payload = {"inputs":
           text}

response = requests.post(API_url,headers=headers,json=payload)
if response.status_code == 200:
    # this will ensure the response is an image
    if 'image' in response.headers.get('Content-Type',''):
        image = Image.open(BytesIO(response.content))
        image.show()
    else:
        print("Error the content type is not an image")
else:
    print(f"Error the status code is = {response.status_code}")    