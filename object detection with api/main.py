from config import hf_api_key
import requests
import os, io, time, random, requests, mimetypes
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont


model = "microsoft/resnet-50"
base_url = "https://router.huggingface.co/hf-inference/models/"
API = base_url+model
ALLOWED, MAX_MB = {".jpg",".jpeg",".png",".bmp",".gif",".webp",".tiff"}, 8
EMOJI = {"person":"🧍","car":"🚗","truck":"🚚","bus":"🚌","bicycle":"🚲","motorcycle":"🏍️","dog":"🐶","cat":"🐱",
         "bird":"🐦","horse":"🐴","sheep":"🐑","cow":"🐮","bear":"🐻","giraffe":"🦒","zebra":"🦓","banana":"🍌",
         "apple":"🍎","orange":"🍊","pizza":"🍕","broccoli":"🥦","book":"📘","laptop":"💻","tv":"📺","bottle":"🧴","cup":"🥤"}


"""User gives image
      ↓
Program sends image to AI
      ↓
AI finds objects
      ↓
Program draws boxes
      ↓
New image is saved
      ↓
Results are printed"""
path = input("Please enter your image here: ")
with open(path,"rb") as fh: by = fh.read()
mime, _ = mimetypes.guess_type(path)
img_bytes = Image.open(io.BytesIO(by)).convert("RGB")
header = {"Authorization":f"Bearer {hf_api_key}", "Content-Type": mime}
response = requests.post(API,headers=header,data=by, timeout=60)
print(response.status_code)