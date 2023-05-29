#!/usr/bin/env python3
"""
SessionAuth module for the API
"""
from api.v1.auth.auth import Auth
from typing import List, TypeVar


import uuid
from api.v1.auth.auth import Auth
from typing import List, TypeVar


class SessionAuth(Auth):
    """Session authentication"""

    user_id_by_session_id = {}

    def __init__(self):
        pass

    def create_session(self, user_id: str = None) -> str:
        """Creates a Session ID for a user_id"""
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id


User = TypeVar('User')


def current_user(self, request=None) -> User:
    """Returns a User object"""
    return None
