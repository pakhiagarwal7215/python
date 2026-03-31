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
imagename = input("Enter the image here:")
if not os.path.exists(imagename):
    print("cannot find the image")
    exit()
else:
    path = Image.open(imagename).convert("RGB")
    inputs = processor(images=path, return_tensors="pt") 
    inputs = {k: v.to(device) for k, v in inputs.items()}
    out = model.generate(**inputs,max_new_tokens=20,repetition_penalty=1.2)
    caption=processor.decode(out[0],skip_special_tokens=True)
    print(caption)
    print("Select your choice.")
    print("1. Caption - 5 words")
    print("2. Description - 30 words")
    print("3. Summary - 50 words")
    print("4. Exit") 
    choice=int(input("enter your choice:"))
    if choice == 1:
        words=caption.strip().split()
        print(" ".join(words[:5])) 
    elif choice == 2:
        words=caption.strip().split()
        print(" ".join(words[:30]))
    elif choice == 3:
        words=caption.strip().split()
        print(" ".join(words[:50]))
    elif choice == 4:
        words=caption.strip().split()
        print("goodbye")
        exit
    else:
        print("not a valid option please type 1,2,3,4")
       