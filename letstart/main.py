from config import HF_API_KEY
import requests
model = "cardiffnlp/twitter-roberta-base-sentiment-latest"
base_URL = "https://router.huggingface.co/hf-inference/models/"
API_url = base_URL+model
headers={"Authorization":f"Bearer {HF_API_KEY}"}
print("----------SENTIMENT ANYLIZER ACTIVATING----------")
sentiment_reference = input("Enter a sentence to analyze: ")
payload={
    "inputs":sentiment_reference
}
response=requests.post(API_url,headers=headers,json=payload)

if response.status_code == 200:
    data = response.json()
    T=data[0]
    print(T)
