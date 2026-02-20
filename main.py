from config import hf_api_key
import requests
model = "facebook/bart-large-mnli"
base_URL = "https://router.huggingface.co/hf-inference/models/"
API_url = base_URL+model

headers={
         "Authorization":f"Bearer {hf_api_key}"
        }
topics=["sports","technology","bussiness", "entertainment","productivity"]

print("Welcome to news headlines! I will guess what topic you are talking about")
Headline = input("Please enter a headline: ")

payload={
    "inputs":Headline,
    "parameters":{"candidate_labels":topics}
}

response=requests.post(API_url,headers=headers,json=payload)

if response.status_code == 200:
    data = response.json()
    T=data[0]
    print(T)
    