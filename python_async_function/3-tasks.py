#!/usr/bin/env python3
"""
This module contains a function that creates a new asyncio.Task from a call to
wait_random with a specified maximum delay. The created Task is returned to
the caller for use in an asyncio event loop.
"""

import asyncio
from typing import Any

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio.Task object that calls wait_random with a specified
    maximum delay.

    Args:
    - max_delay: an integer representing the maximum delay value for the
    wait_random call.

    Returns:
    - An asyncio.Task object created by the asyncio event loop, representing
    the asynchronous execution of wait_random with the specified max_delay
    value.
    """
    loop = asyncio.get_event_loop()
    return loop.create_task(wait_random(max_delay))
