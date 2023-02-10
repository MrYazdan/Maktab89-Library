from datetime import datetime

from peewee import ForeignKeyField, DateTimeField
from core.models import BaseModel
from users.models import User


class Session(BaseModel):
    user = ForeignKeyField(User)
    at = DateTimeField()

