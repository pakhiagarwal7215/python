from hf import generate_response
print("="*20)
print("AI LEARNING ACTIVITY:")
print("="*20)
print("Choose an activity = 1. Bias mitigation 2. token limit handeling")
choice = int(input("enter choice: "))
def bias_mitigation_activity():
    prompt = input("Enter an prompt to look at biases (eg. describe an ideal artist): ")
    response = generate_response(prompt,temperature=0.3,max_tokens=1024)
    print(f"generated response is this{response}")
    nprompt = input("Enter a more neutural prompt (eg. describe the quality of a good artist): ")
    answer = generate_response(nprompt,temperature=0.3,max_tokens=1024)
    print(f"Unbiased prompt is {answer}")
def token_limit():
    prompt = input("enter a long prompt (eg. create a story): ")
    response = generate_response(prompt,temperature=0.3,max_tokens=1024)
    print(f" the response is {response}")
    if len(response)>300:   
        response = response[:300]
        print(f"response is too long response should be {response}")
    nprompt = input("Enter a more consice version of your prompt :")
    response = generate_response(nprompt,temperature=0.3,max_tokens=1024)
    print(f"Shorter response is : {response}")
if choice == 1:
    bias_mitigation_activity()
elif choice == 2:
    token_limit()
