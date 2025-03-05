from abc import ABC, abstractmethod

class Book(ABC):
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"
    
    @abstractmethod
    def check_availability(self):
        pass
    
    @abstractmethod
    def borrow(self):
        pass

class PhysicalBook(Book):
    def __init__(self, title, author, isbn, copies):
        super().__init__(title, author, isbn)
        self.__copies = copies
    
    def check_availability(self):
        return self.__copies > 0
    
    def borrow(self):
        if self.check_availability():
            self.__copies -= 1
            return True
        return False
    
    def return_book(self):
        self.__copies += 1
    
    def get_copies(self):
        return self.__copies

class EBook(Book):
    def check_availability(self):
        return True  
    
    def borrow(self):
        return True 

class User(ABC):
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
    
    @abstractmethod
    def get_borrowing_limit(self):
        pass
    
    def borrow_book(self, book):
        if len(self.borrowed_books) < self.get_borrowing_limit():
            if book.borrow():
                self.borrowed_books.append(book)
                print(f"{self.name} borrowed {book.title}")
                return True
        print(f"{self.name} cannot borrow {book.title}")
        return False
    
    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            if isinstance(book, PhysicalBook):
                book.return_book()
            print(f"{self.name} returned {book.title}")

class Student(User):
    def get_borrowing_limit(self):
        return 3

class Professor(User):
    def get_borrowing_limit(self):
        return 5

class Librarian(User):
    def get_borrowing_limit(self):
        return 0  
    
    def add_book(self, catalog, book):
        catalog.add_book(book)
        print(f"Librarian added {book.title} to catalog")

class BookCatalog:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def search_by_title(self, title):
        return [book for book in self.books if book.title.lower() == title.lower()]
    
    def search_by_author(self, author):
        return [book for book in self.books if book.author.lower() == author.lower()]

if __name__ == "__main__":
   
    book1 = PhysicalBook("The Great Gatsby", "F. Scott Fitzgerald", "123456", 5)
    book2 = EBook("Clean Code", "Robert Martin", "789012")
    
    student = Student("Alice")
    professor = Professor("Bob")
    librarian = Librarian("Carol")
    
    catalog = BookCatalog()
    
    librarian.add_book(catalog, book1)
    librarian.add_book(catalog, book2)
  
    student.borrow_book(book1)
    professor.borrow_book(book2)

    print("Search results:", catalog.search_by_title("Clean Code"))
