#!/usr/bin/env python3

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator that counts the number of times a method is called."""
    key = method.__qualname__  # Unique key for the method

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function that increments the call count and invokes
        the method."""
        self._redis.incr(method.__qualname__)  # Increment the call count
        return method(self, *args, **kwargs)  # Invoke the method
    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator that keeps a history of method inputs and outputs."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function that stores the inputs and outputs in Redis."""
        input_data = str(args)  # Convert input arguments to a string
        self._redis.rpush(method.__qualname__ + ":inputs",
                          input_data)  # Store inputs in Redis

        # Invoke the method and convert output to a string
        output_data = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs",
                          output_data)  # Store output in Redis

        return output_data  # Return the output
    return wrapper


def replay(method: Callable):
    """Decorator that replays the history of a method."""
    r = redis.Redis()  # Redis connection
    method_name = method.__qualname__  # Name of the method
    count = r.get(method_name).decode("utf-8")  # Get the call count from Redis
    # Get the stored inputs from Redis
    inputs = r.lrange(method_name + ":inputs", 0, -1)
    # Get the stored outputs from Redis
    outputs = r.lrange(method_name + ":outputs", 0, -1)

    print("{} was called {} times:".format(method_name, count))

    # Print the inputs and corresponding outputs
    for input_data, output_data in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(method_name, input_data.decode("utf-8"),
                                     output_data.decode("utf-8")))


class Cache():
    """Cache class that provides methods for storing and retrieving data from
    Redis."""

    def __init__(self):
        """Constructor that initializes the Redis connection and clears the
        Redis database."""
        self._redis = redis.Redis()  # Initialize Redis connection
        self._redis.flushdb()  # Clear the Redis database

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Method for storing data in Redis."""
        key = str(uuid.uuid4())  # Generate a unique key
        self._redis.set(key, data)  # Store data in Redis
        return key  # Return the generated key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str,
                                                                    bytes,
                                                                    int,
                                                                    float]:
        """Method for retrieving data from Redis."""
        data = self._redis.get(key)  # Get data from Redis
        if fn:
            # Apply the provided function to the data if specified
            return fn(data)
        return data  # Return the data

    def get_str(self, key: str) -> str:
        """Method for retrieving string data from Redis."""
        return self.get(key, str)  # Call the 'get' method with the 'str'
    function

    def get_int(self, key: str) -> int:
        """Method for retrieving integer data from Redis."""
        return self.get(key, int)  # Call the 'get' method with the 'int'
    function
