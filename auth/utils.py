from datetime import timedelta, datetime

from auth.models import Session
from core.state import StateManager


def check_logged_in_user():
    if sessions := Session.select():
        if session := list(sessions)[0]:
            if session.at + timedelta(minutes=60) > datetime.now():
                StateManager.set_user(session.user)


def session_clear():
    sessions = Session.select()
    for session in sessions:
        session.delete()
