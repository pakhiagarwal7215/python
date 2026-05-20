from hf import generate_response
def prompt_engineering_activity():
    print("🎀Welcome to ai prompt engineering tutorial")
    vague = input("enter a vague prompt: ")
    print("AI's response to vague prompt:")
    print(generate_response(vague))
    specific = input("enter a specific prompt: ")
    print("AI's response to specific prompt:")
    print(generate_response(specific))
    contextaul = input("enter a contextaul prompt: ")
    print("AI's response to contextaul prompt:")
    print(generate_response(contextaul))
if __name__ == "__main__":
    prompt_engineering_activity()   