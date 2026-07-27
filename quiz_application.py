questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. New Delhi", "C. Chennai", "D. Kolkata"],
        "answer": "B"
    },
    {
        "question": "Which language is used for AI and Machine Learning?",
        "options": ["A. HTML", "B. CSS", "C. Python", "D. SQL"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B"
    },
    {
        "question": "How many days are there in a leap year?",
        "options": ["A. 365", "B. 364", "C. 366", "D. 367"],
        "answer": "C"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. define", "C. def", "D. fun"],
        "answer": "C"
    }
]

score = 0

print("===== Python Quiz Application =====")

for i, q in enumerate(questions, start=1):
    print(f"\nQuestion {i}: {q['question']}")
    for option in q["options"]:
        print(option)

    while True:
        user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()
        if user_answer in ["A", "B", "C", "D"]:
            break
        print("Invalid input. Please enter A, B, C, or D.")

    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! Correct answer is {q['answer']}.")

print("\n===== Quiz Finished =====")
print(f"Your Score: {score}/{len(questions)}")

percentage = (score / len(questions)) * 100
print(f"Percentage: {percentage:.2f}%")

if percentage == 100:
    print("Excellent!")
elif percentage >= 80:
    print("Great Job!")
elif percentage >= 60:
    print("Good Effort!")
else:
    print("Keep Practicing!")
