import requests

url = "https://opentdb.com/api.php?amount=5&type=multiple"

response = requests.get(url)

if response.status_code == 200:

    trivia_data = response.json()

    score = 0

    for i, question_data in enumerate(trivia_data["results"]):

        print(f"Question {i + 1}:{question_data['question']}")
        
        options = question_data['incorrect_answers'] + [question_data['correct_answer']]

        options = sorted(options)
        for j , option in enumerate(options):
           print(f"{j + 1}. {option}")
        user_answer = input("your answer(1/2/3/4):")

        if options[int(user_answer) - 1] == question_data["correct_answer"]:
            print("Correct!😊")

        else:
            print(f"Wrong! The correct answer was: {question_data['correct_answer']}")

        print("\n")

        print(f"Your final score: {score}/{len(trivia_data['results'])}")
else:
    print("Failed to retrive trivia")
    exit()