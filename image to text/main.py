import os
from transformers import BlipProcessor, BlipForConditionalGeneration,pipeline
from PIL import Image
import torch
import requests
from io import BytesIO

device = "cuda" if torch.cuda.is_available() else "cpu"
print (device)
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base").to(device)
a=pipeline("text-generation",model="gpt2",tokenizer="gpt2",device=0 if device=="cuda" else -1, return_full_text=True)
print("select your choice ✨:")
print("1. caption (5 words)")
print("2. description(30 words)")
print("3.summary(50 words)")
print("4. exit")

one = input("enter the image:")
if not os.path.exists(one):
    print("Error couldnt find image")
    exit()
else:
    image = Image.open(one).convert("RGB")
    inputs = processor(images=image,return_tensors="pt").to(device)
    out=model.generate(**inputs,max_new_tokens=50)
    caption=processor.decode(out[0],skip_special_tokens=True)
    print(caption)