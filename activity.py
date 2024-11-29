def ask_question(question, correct_answer):
    """Ask a question and check if the user's answer is correct."""
    answer = input(question + " ").strip().lower()
    if answer == correct_answer.lower():
        print("Correct!")
        return 1  # Return 1 point for a correct answer
    else:
        print(f"Wrong! The correct answer was: {correct_answer}")
        return 0  # Return 0 points for an incorrect answer


print("Welcome to the Quiz Game!")
print("Answer the following questions to the best of your ability.")

score = 0  # Keep track of the user's score

# Questions and answers
score += ask_question("What is the capital of France?", "Paris")
score += ask_question("What is 5 + 7?", "12")

# Final score and feedback
print("Quiz complete!")
if score == 2:
    print(f"Excellent! You got all {score} questions right!")
elif score == 1:
    print(f"Good job! You got {score} out of 2 questions correct.")
else:
    print(f"Better luck next time! You got {score} out of 3 questions correct.")


