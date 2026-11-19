class Library:
    def __init__(self):
        self.books = []
        self.borrows = []
        self.book_id = 1

    def book_register(self):
        title = input("Enter book title: ")
        for book in self.books:
            if book["Title"].lower() == " ".join(title.split()).lower():
                print("Book", book["Title"], "is already registered.")
                return

        author = input("Enter Book Author: ")
        available = input("Enter available copies: ")
        book = {
            "ID": "B" + str(self.book_id).zfill(3),
            "Title": " ".join(title.split()),
            "Author": author,
            "Copies": available,
        }

        self.books.append(book)

        print("Book registered successfully.")
        print("Book ID:", book["ID"])

        self.book_id += 1

        product = {"Title": self.books, "Author": author, "Available": available}
        self.books.append(product)
        self.book_id = +1
        print("Book registered succesfully")
        pri

