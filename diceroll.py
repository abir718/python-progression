import random

def roll_dice():
    print("🎲 Dice Roller Simulator")
    
    while True:
        roll = input("Press Enter to roll the dice or type 'q' to quit: ")
        if roll.lower() == 'q':
            print("👋 Thanks for playing!")
            break
        dice = random.randint(1, 6)
        print(f"🧊 You rolled a {dice}!\n")

roll_dice()
