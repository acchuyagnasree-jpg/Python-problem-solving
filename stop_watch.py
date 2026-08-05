import time

elapsed_time = 0
running = False
start_time = 0

while True:
    print("\n--- Stopwatch ---")
    print("1. Start")
    print("2. Stop")
    print("3. Reset")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        if not running:
            start_time = time.time()
            running = True
            print("Stopwatch started.")
        else:
            print("Stopwatch is already running.")

    elif choice == "2":
        if running:
            elapsed_time += time.time() - start_time
            running = False
            print(f"Elapsed Time: {elapsed_time:.2f} seconds")
        else:
            print("Stopwatch is not running.")

    elif choice == "3":
        elapsed_time = 0
        running = False
        print("Stopwatch reset.")

    elif choice == "4":
        if running:
            elapsed_time += time.time() - start_time
        print(f"Final Time: {elapsed_time:.2f} seconds")
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
