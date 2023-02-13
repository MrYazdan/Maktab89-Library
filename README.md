# :book: Maktab89 Simple Library Project

- :snake: Pure [Python](https://github.com/python)

- :world_map: Router, Route, Callback (see [core/router.py](https://github.com/MrYazdan/Maktab89-Library/blob/main/core/router.py))

- 🗂 Casscade routing

- 📦 Packages and Components base

- ⚡ State Management via OOP

- 🎒 [Peewee](https://github.com/coleifer/peewee) ORM

## Try it now!

> Library requires Python >= 3.10

### Install peewee orm:
```bash
pip install -r requirements.txt
```
and just run `main.py`:

```bash
python main.py
```
## Simple menu routing - see `routes.py` :
```python
from core.router import Route, CallBack, Router
from core.state import StateManager

router = Router(
    Route("Main", description="Maktab-89 cli library", epilog="Last Update: 2023-02-10 09:37", children=[
        Route("Library", children=[
            Route("Search in books", CallBack("search", "library.views")),
            Route("Show all books", CallBack("show_all", "library.views")),
            Route("Your books", CallBack("your_books", "library.views"), condition=StateManager.login_status),
            Route("Add book", CallBack("add_book", "library.views"), condition=StateManager.login_status),
        ]),
        Route("Profile", condition=StateManager.login_status, children=[
            Route("Show profile", CallBack("profile", "users.views")),
            Route("Change password", CallBack("change_password", "users.views")),
        ]),
        Route("Login", CallBack("login", "users.views"), condition=lambda: not StateManager.login_status()),
        Route("Logout", CallBack("logout", "users.views"), condition=StateManager.login_status),
        Route("Register", CallBack("register", "users.views"), condition=lambda: not StateManager.login_status()),
        Route("Setting", CallBack("setting", "public.views")),
        Route("About", CallBack("about", "public.views")),
    ])
)
```

