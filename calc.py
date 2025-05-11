def calculator():
    print("🧮 Basic Calculator")
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    operation = input("Enter choice (1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == '1':
        print(f"Result: {num1} + {num2} = {num1 + num2}")
    elif operation == '2':
        print(f"Result: {num1} - {num2} = {num1 - num2}")
    elif operation == '3':
        print(f"Result: {num1} * {num2} = {num1 * num2}")
    elif operation == '4':
        if num2 == 0:
            print("⚠️ Cannot divide by zero.")
        else:
            print(f"Result: {num1} / {num2} = {num1 / num2}")
    else:
        print("❌ Invalid operation choice.")

calculator()
