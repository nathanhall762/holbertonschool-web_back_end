#!/usr/bin/env python3
"""
SessionAuth module for the API
"""
import uuid
from api.v1.auth.auth import Auth
from typing import List, TypeVar


class SessionAuth(Auth):
    """Session authentication"""

    user_id_by_session_id = {}

    def __init__(self):
        pass

    def current_user(self, request=None):
        """Returns a User instance based on a session cookie value"""
        if request is None:
            return None

        session_id = self.session_cookie(request)
        if session_id is None:
            return None

        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None

        return User.get(user_id)

    def create_session(self, user_id: str = None) -> str:
        """Creates a Session ID for a `user_id`"""
        if user_id is None or not isinstance(user_id, str):
            return None
        print(f"User ID: {user_id}")
        session_id = str(uuid.uuid4())
        print(f"Generated Session ID: {session_id}")
        self.user_id_by_session_id[session_id] = user_id
        return session_id


User = TypeVar('User')


def current_user(self, request=None) -> User:
    """Returns a User object"""
    return None
