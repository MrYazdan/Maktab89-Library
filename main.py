from routes import router
from core.models import create_tables
from users.models import User
from library.models import Book
from auth.models import Session

if __name__ == '__main__':
    create_tables([User, Book, Session])
    router()
