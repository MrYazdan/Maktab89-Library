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
