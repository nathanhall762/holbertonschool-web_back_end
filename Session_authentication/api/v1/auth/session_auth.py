#!/usr/bin/env python3
"""
SessionAuth module for the API
"""
from api.v1.auth.auth import Auth
from typing import List, TypeVar


class SessionAuth(Auth):
    """ Session authentication
    """

    def __init__(self):
        pass

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns a User object
        """
        return None
