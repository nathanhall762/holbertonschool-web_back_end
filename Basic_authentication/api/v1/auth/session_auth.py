#!/usr/bin/env python3
"""
SessionAuth module for the API
"""
import uuid
from api.v1.auth.auth import Auth
from typing import List, TypeVar
from models.user import User


class SessionAuth(Auth):
    """Session authentication"""

    user_id_by_session_id = {}

    def current_user(self, request=None):
        """Returns a User instance based on a session cookie value"""
        if request is None:
            print("request is none")
            return None

        session_id = self.session_cookie(request)
        if session_id is None:
            print("session_id is None")
            return None

        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            print("user_id is none")
            return None

        return User.get(user_id)

    def create_session(self, user_id: str = None) -> str:
        """Creates a Session ID for a user_id"""
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Returns a User ID based on a Session ID"""
        if session_id is None or not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)


User = TypeVar('User')