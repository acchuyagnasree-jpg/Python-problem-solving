class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True


class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        self.books.append(Book(title, author))
        print("Book added successfully!")

    def view_books(self):
        if not self.books:
            print("Library is empty.")
            return

        print("\nLibrary Books")
        for i, book in enumerate(self.books, start=1):
            status = "Available" if book.available else "Issued"
            print(f"{i}. {book.title} - {book.author} ({status})")

    def issue_book(self):
        title = input("Enter book title to issue: ")

        for book in self.books:
            if book.title.lower() == title.lower():
                if book.available:
                    book.available = False
                    print("Book issued successfully.")
                else:
                    print("Book is already issued.")
                return

        print("Book not found.")

    def return_book(self):
        title = input("Enter book title to return: ")

        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.available:
                    book.available = True
                    print("Book returned successfully.")
                else:
                    print("Book was not issued.")
                return

        print("Book not found.")


library = Library()

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.add_book()
    elif choice == "2":
        library.view_books()
    elif choice == "3":
        library.issue_book()
    elif choice == "4":
        library.return_book()
    elif choice == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice.")
