#!/usr/bin/env python3
""" module to implement a hash_password function """


import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt with salt.

    Args:
        password (str): The password to be hashed.

    Returns:
        bytes: The salted and hashed password as a byte string.

    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates whether the provided password matches the hashed password.

    Args:
        hashed_password (bytes): The hashed password as a byte string.
        password (str): The password to be validated.

    Returns:
        bool: True if the password matches the hashed password, False
        otherwise.

    """
    return bcrypt.checkpw(password.encode(), hashed_password)
