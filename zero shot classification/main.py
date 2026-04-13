from hf import generate_response
print("ZERO SHOT, ONE SHOT AND FEW SHOT PROMPTS")
category = input("which category(ex. Animal,food,city):")
item = input(f"Enter a specific {category} to classify:")
if not category or not item :
    print("Please fill both fields")
zero_shot = f"Is {item} a {category}? answer(yes/no) " 
print("ZERO SHOT learning response is:",generate_response(zero_shot,temperature=0.3,max_tokens=1024))

one_shot_prompt = f"Example- Category:food item:pizza  answers: yes pizza is a food, now answer Category:{category} and item:{item} what will be your answer?"
print("ONE SHOT learning response is:",generate_response(one_shot_prompt,temperature=0.3,max_tokens=1024))

few_shot_prompt = f"""Example 1: Category: fruit Item: apple Answer: Yes, apple is a fruit.
                    Example 2: Category: animal Item: gorilla Answer: Yes, gorilla is a animal
                    Now you try: Category: {category} Item: {item} Answer:"""
print("FEW SHOT learning response is:",generate_response(few_shot_prompt,temperature=0.3,max_tokens=1024))

#Creative task 
creative_prompt = f"""Write a one-sentence story about the given word. 
                Example 1: Word: moon Story: The moon winked at the lovers as they shared their first kiss. 
              Word: {item} Story:""" 
print("\n--- CREATIVE FEW-SHOT EXAMPLE ---") 
print(f"Response: {generate_response(creative_prompt, temperature=0.7, max_tokens=1024)}")