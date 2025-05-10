import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("Try guessing the number between 1 to 100.")
    
    secret_number = random.randint(1, 100)
    attempts = 0

    while guess != secret_number:
        guess = int(input("🔢 Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("📉 Too low! Try again.")
        elif guess > secret_number:
            print("📈 Too high! Try again.")

    print(f"Congratulations! You guessed it in {attempts} attempts.")

number_guessing_game()
