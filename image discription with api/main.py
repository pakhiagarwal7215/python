#you are loading two AI models:
#BLIP → for image captioning
#GPT-2 → for text generation / description expansion
#from huggingface_hub import login
#login("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")
#pip install huggingface_hub
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


imagename = input("Enter the image here:")
if not os.path.exists(imagename):
    print("cannot find the image")
    exit()
else:
    path = Image.open(imagename).convert("RGB")
    # preparing the image to give to the model
    """
    It performs several preprocessing steps:

        Resize image
        Normalize pixel values
        Convert image → tensor
        Add batch dimension"""
    #images: The image input, usually a PIL Image or a batch of PIL Images.
    inputs = processor(images=path, return_tensors="pt") #processor() returns a dictionary :
    inputs = {k: v.to(device) for k, v in inputs.items()}
    out = model.generate(**inputs, max_new_tokens=20, repetition_penalty=1.2)
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

