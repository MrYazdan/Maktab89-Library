# SQL DBs:
# SQlite => mydb.db -> development - debug
# Postgres => ...
# MariaDB - MySql => ...
# ... => ...


# 1 :
# import sqlite3
#
# con = sqlite3.connect("development.db")
# cur = con.cursor()
#
# cur.execute("CREATE TABLE movie(title, year, score)")
#
# con.commit()

from pony.orm import Database, Required, Set, db_session

db = Database()


class Person(db.Entity):
    name = Required(str)
    age = Required(int)
    cars = Set('Car')

    def __str__(self):
        return f"<Person> name: {self.name}, age: {self.age}, cars: {self.cars}"


class Car(db.Entity):
    make = Required(str)
    model = Required(str)
    owner: Person = Required(Person)

    def __str__(self):
        return f"<Car> model: {self.model}, owner: {self.owner.name}"


db.bind(provider='sqlite', filename='db.sqlite', create_db=True)
db.generate_mapping(create_tables=True)

with db_session:
    # Person(name="Zahra", age=15)
    # Person(name="Alireza", age=28)
    # Person(name="Fatemeh", age=12)
    # Person(name="Yazdan", age=43)
    # Person(name="Ghadir", age=32)

    # yazdan = Person.get(name="yazdan")
    # query = Person.select(lambda p: "yazdan" in p.name.lower())
    # yazdan = query.first()
    #

    # Car(make="US", model="WO3", owner=1)
    # Car(make="IR", model="Pride", owner=1)
    # Car(make="IN", model="Bora", owner=yazdan)

    persons = Person.select(lambda p: True)
    print(*list(persons), sep="\n")

    # persons = Person
