
class Book:
    def __init__(self, title, author, copies_available):
        self.title = title
        self.author = author
        self.copies_available = copies_available


    def display_book(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Copies Available:", self.copies_available)
        print("-----------------------------")

    def borrow_book(self):
        if self.copies_available > 0:
            self.copies_available -= 1
            print("Book borrowed successfully")
        else:
            print("No copies available")


    def return_book(self):
        self.copies_available += 1
        print("Book returned successfully")


book1 = Book("Harry Potter", "J.K. Rowling", 3)
book2 = Book("The Hobbit", "J.R.R. Tolkien", 2)
book3 = Book("Atomic Habits", "James Clear", 1)


print("=== Book 1 ===")
book1.display_book()
book1.borrow_book()
book1.return_book()
book1.display_book()

print("=== Book 2 ===")
book2.display_book()
book2.borrow_book()
book2.return_book()
book2.display_book()

print("=== Book 3 ===")
book3.display_book()
book3.borrow_book()
book3.return_book()
book3.display_book()