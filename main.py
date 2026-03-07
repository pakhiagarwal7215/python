from config import HF_API_KEY
import requests
from colorama import Fore,Style,init
from PIL import Image,ImageEnhance,ImageFilter
from io import BytesIO
from PIL import Image
init(autoreset = True)


model = "stabilityai/stable-diffusion-xl-base-1.0"
base_url = "https://router.huggingface.co/hf-inference/models/"
API_url = base_url+model
prompt = input("Please enter a text :")
headers = {"Authorization":f"Bearer {HF_API_KEY}"}
payload = {"inputs":
           prompt}

response =requests.post(API_url,headers=headers,json=payload)
if response.status_code == 200:
    # this will ensure the response is an image
    
    if 'image' in response.headers.get('Content-Type',''):
        image = Image.open(BytesIO(response.content))
        image.show()
        image.show("orignal_image")
        image.save("orignal.jpg")

        # brightening the image
        enhancer = ImageEnhance.Brightness(image)
        BRIGHT_IMAGE = enhancer.enhance(1.8)
        BRIGHT_IMAGE.show("brightened_image")
        BRIGHT_IMAGE.save("brighter.jpg")
# changing contrast
        enhancer_contrast = ImageEnhance.Contrast(image)

        #>1 (e.g., 1.5, 2)	More contrast (darker, lighter)
        #<1 (e.g., 0.5)	Less contrast (faded)
        
        contrast = enhancer_contrast.enhance(0.5)
        contrast.show("contrast_image")
        contrast.save("contrast.jpg")
    else:
        print("Error the content type is not an image")
        print("Error the result was not an image")
else:
    print(f"Error the status code is = {response.status_code}")    
    print(f"Error the status code was: {response.status_code}")
