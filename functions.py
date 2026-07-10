def calculate(a, b):
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)

    if b != 0:
        print("Division:", a / b)
    else:
        print("Cannot divide by zero")


num1 = 20
num2 = 5

calculate(num1, num2)
