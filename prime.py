def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True

def prime_checker():
    print("Prime Number Checker")
    num = int(input("Enter a number: "))

    if is_prime(num):
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")

prime_checker()
