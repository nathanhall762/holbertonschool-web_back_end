#!/usr/bin/env python3
from bcrypt import checkpw, gensalt, hashpw
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid
from typing import Union


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user and return the User object."""
        try:
            existing_user = self._db.find_user_by(email=email)
            raise ValueError(f"User {existing_user.email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(
                email=email,
                hashed_password=hashed_password
            )
            return user

    def valid_login(self, email: str, password: str) -> bool:
        """Check if the provided email and password are valid for login."""
        try:
            user = self._db.find_user_by(email=email)
            hashed_password = user.hashed_password
            if checkpw(password.encode('utf-8'), hashed_password):
                return True
        except NoResultFound:
            pass
        return False

    def create_session(self, email: str) -> str:
        """Create a new session for the user and return the session ID."""
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def _hash_password(self, password: str) -> str:
        """Hash a password using bcrypt."""
        salt = gensalt()
        hashed_password = hashpw(password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        """ gets user from session id. """
        if session_id is None:
            return None

        user = self._db.find_user_by(session_id=session_id)
        return user if user else None

    def destroy_session(self, user_id: int) -> None:
        """ Destroys a session. """
        self._db.update_user(user_id, session_id=None)


def _generate_uuid() -> str:
    """Generate a new UUID and return it as a string."""
    return str(uuid.uuid4())


def _hash_password(password: str) -> bytes:
    """Hashes a password using bcrypt
    """
    salt = gensalt()
    hashed_password = hashpw(password.encode('utf-8'), salt)
    return hashed_password
