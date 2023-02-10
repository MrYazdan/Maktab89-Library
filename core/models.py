from peewee import SqliteDatabase, Model

db = SqliteDatabase("db.sqlite3")


def create_tables(models: list) -> None:
    with db:
        db.create_tables(models)


class BaseModel(Model):
    class Meta:
        database = db
