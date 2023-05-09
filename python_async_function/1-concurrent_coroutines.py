#!/usr/bin/env python3
# countasync.py
"""
An async routine called wait_n that takes in 2 int arguments (in this order):
n and max_delay.
You will spawn wait_random n times with the specified max_delay.
wait_n should return the list of all the delays (float values).
The list of the delays should be in ascending order without using sort()
because of concurrency.
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay and return the list
    of all the delays.
    The list of the delays should be in ascending order without using sort()
    because of concurrency.

    Args:
    - n (int): the number of times to call the wait_random coroutine
    - max_delay (int): maximum value of delay

    Returns:
    - List[float]: the list of all the delays (float values) in ascending order
    """
    coroutines = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*coroutines)
    return sorted(delays)
