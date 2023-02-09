from core.router import Route, CallBack, Router


router = Router(
    Route("Main", description="Maktab-89 cli library", epilog="Last Update: 2023-02-10 09:37", children=[
        Route("Library", children=[
            Route("Search in books", CallBack("search", "library.views")),
            Route("Show all books", CallBack("show_all", "library.views")),
            Route("Your books", CallBack("your_books", "library.views")),
            Route("Add book", CallBack("add_book", "library.views")),
        ]),
        Route("Profile", CallBack("profile", "users.views")),
        Route("Login", CallBack("login", "users.views")),
        Route("Logout", CallBack("logout", "users.views")),
        Route("Register", CallBack("register", "users.views")),
        Route("Setting", CallBack("setting", "public.views")),
        Route("About", CallBack("About", "public.views")),
    ])
)

