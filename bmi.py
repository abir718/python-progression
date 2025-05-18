def bmi_calculator():
    print("BMI Calculator")

    weight = float(input("Enter your weight in kilograms: "))
    height_cm = float(input("Enter your height in centimeters: "))

    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)

    print(f"\nYour BMI is: {bmi:.2f}")

    if bmi < 18.5:
        print("You are underweight.")
    elif bmi < 24.9:
        print("You have a normal weight.")
    elif bmi < 29.9:
        print("You are overweight.")
    else:
        print("You are obese.")

bmi_calculator()
