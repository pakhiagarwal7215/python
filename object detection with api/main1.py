from config import hf_api_key
import requests
import mimetypes

model = "microsoft/resnet-50"

base_url = "https://router.huggingface.co/hf-inference/models/"
API = base_url + model

path = input("Please enter your image here: ")

# Read image
with open(path, "rb") as f:
    img_bytes = f.read()

# Detect image type
mime, _ = mimetypes.guess_type(path)


if mime is None:
    if path.lower().endswith(".webp"):
        mime = "image/webp"
    else:
        mime = "image/jpeg"
# Headers
header = {
    "Authorization": f"Bearer {hf_api_key}",
    "Content-Type": mime
}

# Send image to AI
response = requests.post(API, headers=header, data=img_bytes, timeout=60)

print("Status Code:", response.status_code)

# Print prediction
if response.status_code == 200:
    print("AI Prediction:")
    data= response.json()
    for item in data:
        print(item["label"])

else:
    print("Error:", response.text)