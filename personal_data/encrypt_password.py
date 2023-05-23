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
