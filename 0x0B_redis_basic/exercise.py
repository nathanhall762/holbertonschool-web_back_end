#!/usr/bin/env python3
import uuid
import redis
from typing import Union


import redis
from typing import Union


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]):
        key = str(uuid.uuid4())  # Generate a unique key using UUID
        self._redis.set(key, data)
        return key

    def get(self, key, fn=None):
        value = self._redis.get(key)
        if value is not None:
            if isinstance(value, bytes):
                # Decode the byte string using UTF-8
                value = value.decode("utf-8")
            if fn is not None and callable(fn):
                return fn(value)
            else:
                return value
        else:
            return None

    def get_str(self, key):
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key):
        return self.get(key, fn=int)


# Testing the implementation
cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value

print("All test cases passed!")
