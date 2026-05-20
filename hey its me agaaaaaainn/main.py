from hf import generate_response
def Reinforcement_learning():
    prompt = input("Please enter a prompt: ")
    response = generate_response(prompt,temperature=0.3,max_tokens=1024)
    print(f"The response is: {response}")
    rating = int(input("Rate the response from 1-5"))
    if rating > 5 and rating < 1:
        print("Invalid choice")
        rating = 3
    feedback = input("Please give me an feedback on how to improve: ")
    nprompt = response+feedback+ f"rating was given {rating} out of five"
    new_response = generate_response(nprompt,temperature=0.3,max_tokens=1024)
    print(f"The improved response is: {new_response}")
def role_based_prompt():
    print("ROLE-BASED PROMPT")
    category = input("What category would you like to discuss about (ex.science,math): ")
    topic = input(f"Enter a specific topic in {category}: ")
    teacher_prompt = f"You are a teacher.explain {topic} in simple terms"
    expert_prompt = f"you are an expert in {category} so explain {topic} in detail and technical manner"
    teacher_response = generate_response(teacher_prompt,temperature=0.3,max_tokens=1024)
    expert_response = generate_response(expert_prompt,temperature=0.3,max_tokens=1024)
    print(f"the teacher response is: {teacher_response}")
    print(f"the expert response is: {expert_response}")
print("AI LEARNING ACTIVITY: ")
print("choose an activity: ")
print(" 1)Reinforcement learning,2)Role-based prompts")
choice = input("enter your choice:")
if choice == "1":
    Reinforcement_learning()
elif choice == "2":
    role_based_prompt()
else:
    print("Please enter a valid choice")