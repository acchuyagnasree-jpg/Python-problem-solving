temperature = float(input("Enter temperature: "))
choice = input("Convert to (C/F): ").upper()

if choice == "C":
    result = (temperature - 32) * 5 / 9
    print("Celsius:", round(result, 2))

elif choice == "F":
    result = (temperature * 9 / 5) + 32
    print("Fahrenheit:", round(result, 2))

else:
    print("Invalid choice")
