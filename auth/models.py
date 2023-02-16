from peewee import ForeignKeyField, DateTimeField
from core.models import BaseModel, create_tables
from users.models import User


class Session(BaseModel):
    user = ForeignKeyField(User)
    at = DateTimeField()


create_tables([Session])
