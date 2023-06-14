#!/usr/bin/env python3
import uuid
import redis
from typing import Union


class Cache:
    def __init__(self): -> None:
        # Create an instance of the Redis client and store it as a private
        # variable
        self._redis = redis.Redis()

        # Flush the Redis instance to clear any existing data
        self._redis.flushdb()

    def store((self,
               data) Union[str,
                           bytes,
                           int,
                           float]) -> str:
        # Generate a random key using uuid
        key = str(uuid.uuid4())

        # Store the input data in Redis using the random key
        self._redis.set(key, data)

        # Return the key as a string
        return key
