class Book:
    def __init__(self, title, author, id, available, catagory = True):
        self.title = title
        self.author = author
        self.id = id
        self.catagory = catagory
        self.available = available

books = []

def add_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    id = input("Enter book ID: ")
    catagory = input("Enter catagory: ")
    book = Book(title, author, id, catagory)
    books.append(book)
    print("Book added successfully!")

def search_book():
    title = input("Enter book title to search: ")
    for book in books:
        if book.title.lower() == title.lower():
            print("Book found:")
            print("Title:", book.title)
            print("Author:", book.author)
            print("ID:", book.id)
            print("catagory:", book.catagory)
            print("Available:", book.available)
            return
    print("Book not found!")

def display_books():
    if not books:
        print("No books available!")
    else:
        print("Available books:")
        for book in books:
            print("Title:", book.title)
            print("Author:", book.author)
            print("ID:", book.id)
            print("catagory:", book.catagory)
            print("Available:", book.available)
            print()

while True:
    print("Menu:")
    print("1. Add a book")
    print("2. Search for a book")
    print("3. Display all books")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        add_book()
    elif choice == "2":
        search_book()
    elif choice == "3":
        display_books()
    elif choice == "4":
        break
    else:
        print("Invalid choice!")
