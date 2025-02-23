from abc import ABC, abstractmethod
from task1 import setup_logger

logger = None


class Book:
    def __init__(self, title: str, author: str, year: str):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def get_books(self) -> list:
        pass


class Library(LibraryInterface):
    def __init__(self):
        self._books = []

    def add_book(self, book: Book) -> None:
        self._books.append(book)

    def remove_book(self, title: str) -> None:
        for b in self._books:
            if b.title == title:
                self._books.remove(b)
                break

    def get_books(self) -> list:
        return self._books


class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self._library = library

    def add_book(self, title: str, author: str, year: str):
        book = Book(title, author, year)
        self._library.add_book(book)
        logger.info(f"Added book: {book}")

    def remove_book(self, title: str):
        self._library.remove_book(title)
        logger.info(f"Removed book with title: {title}")

    def show_books(self):
        books = self._library.get_books()
        if not books:
            logger.info("Library is empty.")
        else:
            for book in books:
                logger.info(book)


def main():
    global logger
    logger = setup_logger("task2")
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                logger.info("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
