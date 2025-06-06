import random
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_upper else ''
    digits = string.digits if use_digits else ''
    symbols = string.punctuation if use_symbols else ''
    
    all_chars = lower + upper + digits + symbols
    
    if not all_chars:
        return "Error: No character types selected."
    
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    print("Password Generator")

    try:
        length = int(input("Enter password length (default 12): ") or 12)
    except ValueError:
        length = 12

    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, use_upper, use_digits, use_symbols)
    print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()