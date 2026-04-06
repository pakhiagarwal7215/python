#from groq import generate_response 
from hf import generate_response
def prompt_engineering_activity():
    print("🎀Welcome to the AI Promt engenieering tutorial")

    vague = input("enter a vague prompt: ")
    print("\nAI's response to vague prompt:")
    print(generate_response(vague))
    specific = input("Enter a specific prompt: ")
    print("\nAI's response to specific prompt:")
    print(generate_response(specific))
    context = input("Enter a contextual prompt: ")
    print("\nAI's response to contextual prompt:")
    print(generate_response(context))

if __name__ == "__main__":
    prompt_engineering_activity()