from os import system as terminal, name as os_name


def clear() -> None:
    terminal("cls" if os_name.lower() == "nt" else "clear")


def banner(name: str) -> None:
    clear()
    print("=" * 42, name.title().center(42), "=" * 42, sep="\n")
