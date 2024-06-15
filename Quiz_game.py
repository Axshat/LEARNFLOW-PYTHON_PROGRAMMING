import random

# Define quiz questions for different difficulty levels
quiz_data = {
    "easy": [
        {"question": "What is the capital of France?", "answer": "Paris"},
        {"question": "What is 2 + 2?", "answer": "4"},
        {"question": "What is the color of the sky?", "answer": "blue"}
    ],
    "medium": [
        {"question": "What is the square root of 16?", "answer": "4"},
        {"question": "Who wrote 'To Kill a Mockingbird'?", "answer": "Harper Lee"},
        {"question": "What is the chemical symbol for water?", "answer": "H2O"}
    ],
    "hard": [
        {"question": "What is the value of pi to 3 decimal places?", "answer": "3.142"},
        {"question": "What year did the Titanic sink?", "answer": "1912"},
        {"question": "Who developed the theory of relativity?", "answer": "Einstein"}
    ]
}

def get_questions(difficulty):
    if difficulty in quiz_data:
        return quiz_data[difficulty]
    else:
        print("Invalid difficulty level! Defaulting to easy.")
        return quiz_data["easy"]

def quiz_game():
    print("Welcome to the Quiz Game!")
    difficulty = input("Select difficulty (easy/medium/hard): ").lower()
    
    questions = get_questions(difficulty)
    random.shuffle(questions)
    
    score = 0
    for i, q in enumerate(questions):
        print(f"Question {i + 1}: {q['question']}")
        answer = input("Your answer: ").strip().lower()
        if answer == q['answer'].lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! The correct answer is: {q['answer']}\n")
    
    print(f"Quiz Over! Your final score is {score} out of {len(questions)}.")

if __name__ == "__main__":
    quiz_game()
