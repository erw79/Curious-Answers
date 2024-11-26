import random

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    
    # List of choices
    choices = ["rock", "paper", "scissors"]
    
    # Ask the user for their choice
    user_choice = input("Enter 'rock', 'paper', or 'scissors': ").lower()
    
    # Check if the user's input is valid
    if user_choice not in choices:
        print("Invalid choice! Please enter 'rock', 'paper', or 'scissors'.")
        return
    
    # Randomly select the computer's choice
    computer_choice = random.choice(choices)
    print(f"The computer chose: {computer_choice}")
    
    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")
        
# Start the game
play_game()
