questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Which language is primarily used for AI and Machine Learning?",
        "options": ["A. Python", "B. HTML", "C. CSS", "D. XML"],
        "answer": "A"
    },
    {
        "question": "How many bits are in one byte?",
        "options": ["A. 4", "B. 8", "C. 16", "D. 32"],
        "answer": "B"
    },
    {
        "question": "Which command is used to initialize a Git repository?",
        "options": ["A. git start", "B. git begin", "C. git init", "D. git create"],
        "answer": "C"
    },
    {
        "question": "Which data type stores True or False values?",
        "options": ["A. int", "B. bool", "C. float", "D. string"],
        "answer": "B"
    }
]

score = 0

print("===== Python Quiz App =====\n")

for index, question in enumerate(questions, start=1):
    print(f"Question {index}: {question['question']}")

    for option in question["options"]:
        print(option)

    user_answer = input("Your answer: ").strip().upper()

    if user_answer == question["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer: {question['answer']}\n")

print("=" * 30)
print(f"Final Score: {score}/{len(questions)}")

percentage = (score / len(questions)) * 100
print(f"Percentage: {percentage:.1f}%")

if percentage >= 80:
    print("Excellent!")
elif percentage >= 60:
    print("Good job!")
else:
    print("Keep practicing!")
