from core.state import StateManager
from core.utils import banner
from core.views import try_again
from library.models import Book
from users.models import User


def search(route):
    pass


def show_all(route):
    pass


def your_books(route):
    try:
        books = Book.select().where(Book.author == StateManager.get_user())

        print()
        for book in books:
            print(f"- Name: {book.name}")
            print(f"- Author: {book.author.username}")
            print(f"- Pages count: {book.pages}")
            print(20 * "-")
    except (Exception, KeyboardInterrupt, AssertionError) as e:
        banner("Error")
        print(e)

        try_again(your_books, route)


def add_book(route):
    try:
        name = input("Please enter book name : ").strip()
        assert name, "Book name should not be empty !"

        author = input("Please enter author username : ").lower()
        assert author, "Author should not be empty !"

        pages = input("Please enter author pages count : ")
        assert pages, "Page should not be empty !"
        assert pages.isnumeric(), "Page should be numeric !"
        assert int(pages) > 0, "Page should not be negative !"
        pages = int(pages)

        author = User.get(User.username == author)

        book = Book.create(
            name=name,
            author=author,
            pages=pages
        )

        print("\n- Your books added -> Info:")
        print(f"- Name: {book.name}")
        print(f"- Author: {book.author.username} - AuthorID: {book.author.id}")
        print(f"- Pages count: {book.pages}")
    except (Exception, KeyboardInterrupt, AssertionError) as e:
        banner("Error")
        print(e)

        try_again(add_book, route)

