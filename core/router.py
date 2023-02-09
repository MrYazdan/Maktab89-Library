from typing import Callable
from importlib import import_module


class Router:
    """
        routes: List[Route]
    """
    pass


class CallBack:
    """
        package: None | str
        function: str | Callable
        arg & kwargs
    """

    def __init__(self, function: str | Callable, package: None | str = None, *args, **kwargs):
        self.function = getattr(
            import_module(package or __name__),
            function if isinstance(function, str) else function.__name__
        )

        self.kwargs = kwargs
        self.args = args

    def __call__(self, *args, **kwargs):
        self.function(*self.args, *args, **self.kwargs, **kwargs)


class Route:
    """
        name: str,
        callback: Callback | None,
        description: str | None,
        epilog: str | None,
        parent: Optional,
        children: None | List[Route]
    """


# Test:

def hi(name=None, freeze=False):
    print("HIIIIIIIIIIIIII")
    if name and freeze:
        print(f"Name ! = {name}")


# c1 = CallBack(hi, name="reza")
# c1(freeze=True)

c1 = CallBack("hi", name="reza")
# c1 = CallBack("salam", "file.views")
c1()
