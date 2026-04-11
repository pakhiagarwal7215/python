import requests
from config import hf_api_key
model = "facebook/bart-large-mnli"
api = f"https://router.huggingface.co/hf-inference/models/{model}"
headers = {"Authorization":f"Bearer {hf_api_key}"}
labels = ["Spam","Safe"]
def classify_message(message):
    payload = {
        "inputs":message,
        "parameters":{"candidate_labels":labels}
        }
    response = requests.post(api,headers=headers,json=payload)
    if not response.ok:
        raise RuntimeError(f"API error:{response.status_code}")
    data = response.json()
    print(data)
    return data[0]['label']
    
def show_results(message, results):
    label, score = results[0]  # Get top prediction
    print("Spam vs Safe Message Classifier")
    print(f"Message: {message}")
    print(f"Result: {label} ({score*100:.1f}%)\n")
    print("Confidence scores:")
    for i,(lbl,scr) in enumerate(results,1):
        print(f"{i}.{lbl}:{scr*100:.1f}%")
    if label == "Spam":
        print("⚠️Dont click links or share personal info!")
    else:
        print("✨Looks safe but still stay alert")
def main():
    print("spam vs safe message classifier")
    print("Type'exit' to quit")
    while True:
        msg = input("enter message:").strip()
        if msg.lower()=="exit":
            print("goodbye!")
            break
        if not msg:
            print("please enter a message")
            continue
        try:
            results = classify_message(msg)
            print(results)
        except Exception as e:
            print(f"Error:{e}")
            print("check your Api key and internet connection")
if __name__=="__main__":
    main()
    