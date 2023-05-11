#!/usr/bin/env python3
'''
A module that contains a single function task_wait_n
'''

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times with max_delay and return a list of the resulting delays.

    Args:
    - n: The number of times to call task_wait_random.
    - max_delay: The maximum value for each call to task_wait_random.

    Returns:
    - A list of floats, representing the resulting delays of each call to task_wait_random.
    """


    coroutines = [task_wait_random(max_delay) for _ in range(n)]
    delays = []
    for coroutine in asyncio.as_completed(coroutines):
        delay = await coroutine
        delays.append(delay)

    return delays
