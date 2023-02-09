class Router:
    """
        routes: List[Route]
    """
    pass


class CallBack:
    """
        package: None | str
        callable: str | Callable
        arg & kwargs
    """
    pass


class Route:
    """
        name: str,
        callback: Callback | None,
        description: str | None,
        epilog: str | None,
        parent: Optional,
        children: None | List[Route]
    """
