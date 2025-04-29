import random

print("Welcome to Rock, Paper, Scissors!")
user_choice = input("Enter rock, paper, or scissors: ").lower()
options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)

print(f"You chose: {user_choice}")
print(f"Computer chose: {computer_choice}")

if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "rock" and computer_choice == "scissors":
    print("You win!")
elif user_choice == "paper" and computer_choice == "rock":
    print("You win!")
elif user_choice == "scissors" and computer_choice == "paper":
    print("You win!")
elif user_choice == "rock" and computer_choice == "paper":
    print("You lose!")
elif user_choice == "paper" and computer_choice == "scissors":
    print("You lose!")
elif user_choice == "scissors" and computer_choice == "rock":
    print("You lose!")
else:
    print("Invalid input.")
