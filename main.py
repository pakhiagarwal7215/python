from config import hf_api_key
import requests
from PIL import Image,ImageEnhance,ImageFilter
from io import BytesIO


model = "stabilityai/stable-diffusion-xl-base-1.0"
base_url = "https://router.huggingface.co/hf-inference/models/"
API_url = base_url +model

prompt = input("Please enter a text :")
headers = {"Authorization":f"Bearer {hf_api_key}"}
payload = {"inputs":
           prompt}

response =requests.post(API_url,headers=headers,json=payload)

if response.status_code == 200:
    
    if 'image' in response.headers.get('Content-Type',''):
        image = Image.open(BytesIO(response.content))
        image.show(title="ORIGNAL IMAGE")
        image.save("o.jpg")

        # brightening the image
        enhancer = ImageEnhance.Brightness(image)
        BRIGHT_IMAGE = enhancer.enhance(1.8)
        BRIGHT_IMAGE.show(title="BRIGHTENED IMAGE")
        BRIGHT_IMAGE.save("b.jpg")

        # changing contrast
        enhancer_contrast = ImageEnhance.Contrast(image)
        #Factor	Effect 0	Gray image (no contrast)
        #1	Original image
        #>1 (e.g., 1.5, 2)	More contrast (darks darker, lights lighter)
        #<1 (e.g., 0.5)	Less contrast (image looks faded)
        
        contrast = enhancer_contrast.enhance(0.5)
        contrast.show(title="CONTRAST IMAGE")
        contrast.save("c.jpg")
    else:
        print("Error the result was not an image")
else:
    print(f"Error the status code was: {response.status_code}")