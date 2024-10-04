class Book:
    
    def __init__(self, title, author):
        self.title = title        
        self.author = author      
        self._is_checked_out = False  

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out

    def __str__(self):
        status = "Available" if self.is_available() else "Checked Out"
        return f"{self.title} by {self.author} ({status})"


class Library:
    
    def __init__(self):
        self._books = []  

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    return f"You have checked out '{title}'."
                else:
                    return f"'{title}' is already checked out."
        return f"'{title}' not found in the library."

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    return f"You have returned '{title}'."
                else:
                    return f"'{title}' was not checked out."
        return f"'{title}' not found in the library."

    def list_available_books(self):
        available_books = [str(book) for book in self._books if book.is_available()]
        if available_books:
            return "\n".join(available_books)
        return "No books are currently available."


if __name__ == "__main__":
    library = Library()
    
    book1 = Book("Brave New World", "Aldous Huxley")
    book2 = Book("1984", "George Orwell")

    library.add_book(book1)
    library.add_book(book2)

    print("Available books after setup:")
    print(library.list_available_books())

    print("\n", library.check_out_book("1984"))

    print("\nAvailable books after checking out '1984':")
    print(library.list_available_books())

    print("\n", library.return_book("1984"))

    print("\nAvailable books after returning '1984':")
    print(library.list_available_books())
