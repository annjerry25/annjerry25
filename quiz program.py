questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Paris", "London", "Rome"],
        "answer": "Paris"
    },
    # Add more questions in a similar format
]
def run_quiz(questions):
    score = 0
    for idx, question in enumerate(questions, start=1):
        print(f"\nQuestion {idx}: {question['question']}")
        for i, option in enumerate(question['options'], start=1):
            print(f"{i}. {option}")

        user_answer = input("Your answer (enter the option number): ")

        if user_answer.isdigit() and 1 <= int(user_answer) <= len(question['options']):
            user_answer = question['options'][int(user_answer) - 1]

        if user_answer.lower() == question['answer'].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question['answer']}")

    print(f"\nQuiz completed! Your score is: {score}/{len(questions)}")

# Call the function
run_quiz(questions)
