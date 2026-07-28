import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password


def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(char in string.punctuation for char in password):
        score += 1

    if score <= 2:
        return "Weak Password"

    elif score <= 4:
        return "Medium Password"

    else:
        return "Strong Password"


def main():
    print("Password Generator")

    length = int(input("Enter password length: "))

    password = generate_password(length)

    print("\nGenerated Password:", password)

    result = check_strength(password)

    print("Password Strength:", result)


main()
