import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

while True:
    user = input("\nEnter Rock, Paper, or Scissors (or 'quit' to exit): ").lower()

    if user == "quit":
        break

    if user not in choices:
        print("Invalid choice! Try again.")
        continue

    computer = random.choice(choices)

    print("You chose:", user)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a Tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You Win!")
        user_score += 1
    else:
        print("Computer Wins!")
        computer_score += 1

    print(f"Score -> You: {user_score} | Computer: {computer_score}")

print("\nFinal Score")
print("You:", user_score)
print("Computer:", computer_score)

if user_score > computer_score:
    print("Overall Winner: You!")
elif computer_score > user_score:
    print("Overall Winner: Computer!")
else:
    print("Match Draw!")
