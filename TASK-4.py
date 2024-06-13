# ROCK , PAPER , SCISSOR GAME

import random

def get_user_choice():
    while True:
        user_choice = input("Enter rock, paper, or scissors: ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please enter rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You loses!"

def display(user_choice, computer_choice, result):
    print(f"Your choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    print(result)

def play_game():
    user_score = 0
    computer_score = 0
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = winner(user_choice, computer_choice)
        display(user_choice, computer_choice, result)

        if "win" in result:
            user_score += 1
        elif "lose" in result:
            computer_score += 1

        print("Scores") 
        print(f"You: {user_score} ,Computer: {computer_score} ")     
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break


play_game()
