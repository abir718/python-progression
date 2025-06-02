questions = [
    {"q": "What is the capital of France?", "a": "paris"},
    {"q": "What is 5 * 6?", "a": "30"},
    {"q": "What color do you get when you mix red and white?", "a": "pink"},
    {"q": "Which planet is known as the Red Planet?", "a": "mars"},
    {"q": "What is the square root of 64?", "a": "8"},
    {"q": "Who wrote 'Romeo and Juliet'?", "a": "shakespeare"},
    {"q": "What is the chemical symbol for water?", "a": "h2o"},
    {"q": "What is the tallest mountain in the world?", "a": "everest"},
    {"q": "How many continents are there?", "a": "7"},
    {"q": "What gas do plants absorb from the atmosphere?", "a": "carbon dioxide"},
]

score = 0

for q in questions:
    ans = input(q["q"] + " ").strip().lower()
    if ans == q["a"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer was '{q['a']}'.")

print(f"\nYour final score: {score}/{len(questions)}")
