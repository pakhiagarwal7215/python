import os
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration, pipeline
from io import BytesIO
import torch
import requests
device = "cuda" if torch.cuda.is_available() else "cpu"
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base").to(device)
a = pipeline("text-generation",model="gpt2",tokenizer="gpt2",device = 0 if device=="cuda" else -1,return_full_text=True)
print("Select your choice.")
print("1. Caption - 5 words")
print("2. Description - 30 words")
print("3. Summary - 50 words")
print("4. Exit") 
imagename = input("Enter the image here:")
if not os.path.exists(imagename):
    print("cannot find the image")
    exit()
else:
    image = Image.open(imagename).convert("RGB")
    inputs = processor(images=image, return_tensors="pt").to(device)
    out = model.generate(**inputs,max_new_tokens=20,repetition_penalty=1.2)
    caption=processor.decode(out[0],skip_special_tokens=True)
    print(caption)