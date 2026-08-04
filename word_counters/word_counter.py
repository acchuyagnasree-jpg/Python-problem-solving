text = input("Enter a sentence or paragraph:\n")

words = text.split()

word_count = len(words)
char_count = len(text)
char_no_spaces = len(text.replace(" ", ""))

print("\n----- Result -----")
print("Total Words:", word_count)
print("Total Characters:", char_count)
print("Characters (without spaces):", char_no_spaces)
