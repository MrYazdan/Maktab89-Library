from datetime import datetime
from hashlib import md5
from getpass import getpass

from auth.models import Session
from auth.utils import session_clear
from core.state import StateManager
from core.utils import banner
from core.views import try_again
from users.models import User


def login(route):
    try:
        username = input("Please enter your username : ").lower()
        assert username, "Username should not be empty !"

        password = getpass("Please enter your password : ")
        assert password, "Password should not be empty !"

        password = md5(password.encode()).hexdigest()

        user = User.get(
            (User.username == username) &
            (User.password == password)
        )

        StateManager.set_user(user)

        session_clear()

        Session.create(
            user=user,
            at=datetime.now()
        )

        print("\n- Login successful ✅")
        print(f"- Welcome {user.username}\n")

    except (Exception, KeyboardInterrupt, AssertionError) as e:
        banner("Error")
        print(str(e).split("\n")[0][:-1])

        try_again(login, route)


def logout(route):
    StateManager.logout()
    print("\n- Logout successful")


def profile(route):
    try:
        user = StateManager.get_user()
        print(f"Username : {user.username}")

    except (Exception, KeyboardInterrupt, AssertionError) as e:
        banner("Error")
        print(str(e).split("\n")[0][:-1])

        logout(route.parent)


def change_password(route):
    try:
        old_password = getpass("Please enter your old password : ")
        assert old_password, "Old password should not be empty !"

        password = getpass("Please enter your password : ")
        assert password, "Password should not be empty !"

        confirm_password = getpass("Please enter confirm password : ")
        assert confirm_password, "Confirm password should not be empty !"
        assert confirm_password == password, "Confirm password and password does not match !"

        old_password = md5(old_password.encode()).hexdigest()
        password = md5(password.encode()).hexdigest()

        user = StateManager.get_user()

        assert user.password == old_password, "Password incorrect"

        user.password = password
        user.save()

        print("- Change password successful ✅\n")
    except (Exception, KeyboardInterrupt, AssertionError) as e:
        banner("Error")
        print(e)

        try_again(register, route)


def register(route):
    try:
        username = input("Please enter your username : ").lower()
        assert username, "Username should not be empty !"

        password = getpass("Please enter your password : ")
        assert password, "Password should not be empty !"

        confirm_password = getpass("Please enter confirm password : ")
        assert confirm_password, "Confirm password should not be empty !"
        assert confirm_password == password, "Confirm password and password does not match !"

        password = md5(password.encode()).hexdigest()

        User.create(
            username=username,
            password=password
        )

        print("- Registration successful ✅\n")
    except (Exception, KeyboardInterrupt, AssertionError) as e:
        banner("Error")
        print(e)

        try_again(register, route)
