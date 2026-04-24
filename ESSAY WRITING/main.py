from hf import generate_response
print("="*20)
print("AI ESSAY WRITING ASSISTANT")
print("="*20)
topic = input("What is the topic for your essay?: ")
essay_type = input("What kind of essay are you writing: ")
lenght = ["300","1000","1200","1300","2000"]
print("Select how many words should be there in your essay: ")
for i in lenght :
    print(i)
lenght = input("Enter any of the choices from above: ")
target = input("Who is your audience? (eg. college students,teacher,work): ")
if not topic:
    topic = "art"
if not essay_type:
    essay_type = "narrative essay type"
if not lenght:
    lenght = "300"
if not target:
    target = "teacher"
temprature = float(input("Enter the temprature 0.1 - 0.3 for formal and structured writing, 0.6 - 0.7 for creative and expressive response"))
if temprature < 0.1 or temprature > 1:
    print("Invalid input: setting tempratrure to 0.3")
    temprature = "0.3"
prompt = f"Write an introduction for an {essay_type} essay on the topic {topic} limited to {lenght} words" 
response = generate_response(prompt,temprature,max_tokens=1024)
print(f"generated response is this {response}")
print("Would you like the body of the essay to be a full draft or step by step :")
print("1. full draft 2. step by step")
choice = int(input("Enter your choice 1 or 2: "))
if choice == 1:
    prompt = f"write a full body for an essay on {topic} with the stance of {target}"
    response = generate_response(prompt,temprature,max_tokens=1024)
    print(f"Newly generated response is {response}")
else:
    prompt = f"Write a step by step argumentive essay on {topic} give evidence and reasoning"
    response = generate_response(prompt,temprature,max_tokens=1024)
    print(f"Newly generated response is {response}")