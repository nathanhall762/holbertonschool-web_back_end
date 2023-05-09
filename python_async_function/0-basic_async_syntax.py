#!/usr/bin/env python3
# countasync.py
"""
This module contains an asynchronous coroutine named
`wait_random` that takes in an integer argument
`max_delay` (with a default value of 10) and waits for
a random delay between 0 and `max_delay` (included and
float value) seconds before eventually returning the
delay time.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and
    max_delay seconds (included).

    Args:
        max_delay (int): The maximum delay in seconds. Default is 10.

    Returns:
        float: A float representing the actual delay in seconds.
    """
    actual_delay = random.uniform(0, max_delay)
    await asyncio.sleep(actual_delay)
    return actual_delay
