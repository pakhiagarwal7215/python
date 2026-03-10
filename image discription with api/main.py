#you are loading two AI models:
#BLIP → for image captioning
#GPT-2 → for text generation / description expansion

import os #File handling
from PIL import Image
#HuggingFace models - transformers
from transformers import BlipProcessor, BlipForConditionalGeneration, pipeline
from io import BytesIO
import torch
import requests

#Detecting GPU or CPU
device = "cuda" if torch.cuda.is_available() else "cpu"
#loading the blip processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
# uploading the BLIP model
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base").to(device)
# loading gpt 2

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
    # preparing the image to give to the model
    """
    It performs several preprocessing steps:

        Resize image
        Normalize pixel values
        Convert image → tensor
        Add batch dimension"""

    #images: The image input, usually a PIL Image or a batch of PIL Images.
    inputs = processor(images=image, return_tensors="pt").to(device)
    out = model.generate(**inputs, max_new_tokens=50) #output will be in the form of tokens
    caption = processor.decode(out[0], skip_special_tokens = True) #converting tokens to text
    print(caption)
