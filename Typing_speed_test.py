import time

sentence = "Python is a powerful programming language."

print(sentence)
input("Press Enter to start...")

start = time.time()
typed = input("Type here: ")
end = time.time()

time_taken = end - start
words = len(typed.split())

print(f"Time: {time_taken:.2f} seconds")
print(f"WPM: {(words/time_taken)*60:.2f}")
