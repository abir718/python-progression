def unit_converter():
    print("Unit Converter")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")

    choice = input("Choose conversion (1 or 2): ")
    value = float(input("Enter the distance: "))

    if choice == '1':
        miles = value * 0.621371
        print(f"{value} km = {miles:.2f} miles")
    elif choice == '2':
        km = value / 0.621371
        print(f"{value} miles = {km:.2f} km")
    else:
        print("Invalid choice.")

unit_converter()
