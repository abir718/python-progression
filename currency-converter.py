def convert_currency(amount, from_currency, to_currency):
    rates = {
        'USD': 1.0,
        'EUR': 0.93,
        'GBP': 0.79,
        'INR': 83.12,
        'JPY': 155.69,
        'CAD': 1.38,
        'AUD': 1.50,
    }

    if from_currency not in rates or to_currency not in rates:
        print("Hmm, I don’t recognize that currency.")
        return None

    usd = amount / rates[from_currency]
    converted = usd * rates[to_currency]
    return converted

def main():
    print("Welcome to the Currency Converter!")
    print("You can convert between: USD, EUR, GBP, INR, JPY, CAD, AUD")
    
    try:
        amount = float(input("How much money do you want to convert? "))
        from_currency = input("What's the currency now? ").upper()
        to_currency = input("What do you want it in? ").upper()

        result = convert_currency(amount, from_currency, to_currency)
        if result is not None:
            print(f"{amount} {from_currency} is about {result:.2f} {to_currency}")
    except ValueError:
        print("That doesn’t look like a number. Try again.")

if __name__ == "__main__":
    main()
