# A dictionary that stores questions and answers
# Have a variable that tracks the score of the player
# loop through the dictionary using the key values pairs
# display each question to the user and allow them to answer
# tell them if they are right or wrong
# show the final reuslt when quiz is completed

quiz = {
    "option_1": {
        "question": "What is the capital of France",
        "answer": "Paris"
    },
    "option_2": {
        "question": "What is the capital of Germany",
        "answer": "Berlin"
    },
    "option_3": {
        "question": "What is the capital of Italy",
        "answer": "Rome"
    },
    "option_4": {
        "question": "What is the capital of Spain",
        "answer": "Madrid"
    },
    "option_5": {
        "question": "What is the capital of Argentina",
        "answer": "Buenos Aires"
    },
    "option_6": {
        "question": "What is the capital of Chile",
        "answer": "Santiago"
    },
    "option_7": {
        "question": "What is the capital of Uruguay",
        "answer": "Montevideo"
    },
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input('Your answer:')

    if answer.lower() == value['answer'].lower():
        print(" " * 20)
        print("Correct!")
        score += 1
        print (f"Your score is {score}")
        print(" " * 20)
    else:
        print(" " * 20)
        print("Wrong!")
        print(f"The correct answer is {value['answer']}")
        print (f"Your score is {score}")
        print(" " * 20)


print(" " * 20)

print("=" * 60)
print(" " * 20)

print(f"You got {score} out of 7 questions correctly")
print(f"Your percentaje is {int((score/7) * 100)}%")

print(" " * 20)
print("=" * 60)
print(" " * 20)