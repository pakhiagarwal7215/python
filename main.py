import requests
import random
EDUCATION_CATEGORY_ID = 9
API_URL = f"https://opentdb.com/api.php?amount=10&category={EDUCATION_CATEGORY_ID}&type=multiple"
options = []
response = requests.get(API_URL)
if response.status_code == 200:
    data = response.json()
    for i, qdata in enumerate(data["results"]):
        print("question", i+1)
        print(qdata["question"])
        correct=qdata["correct_answer"]
        options = qdata["incorrect_answers"]+[qdata["correct_answer"]]
        options = sorted(options)
        for j , opt in enumerate(options):
            print(j+1, opt) 
        choice = int(input("enter your answer 1, 2, 3 or 4  "))
        if  choice<1 or choice >4:
            print("You have entered invalid choice")
        else:
            if options[choice-1] == correct:
                print("Correct!")
            else:
                print("incorrect")