from core.utils import banner


def try_again(function, route):
    cmd = input("\nTry again ? [Y|n] : ") or "y"
    if cmd.strip().lower()[0] != "n":
        # Yes -> try again
        banner(route.name.title())
        function(route)
    else:
        # No -> back
        route.parent()
