from peewee import CharField, ForeignKeyField, IntegerField
from core.models import BaseModel
from users.models import User


class Book(BaseModel):
    name = CharField()
    author = ForeignKeyField(User)
    pages = IntegerField()

    def __str__(self):
        return f"<B:{self.id}> name: {self.name}, author: {self.author}, pages: {self.pages}"
