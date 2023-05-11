#!/usr/bin/env python3
"""
This module defines a coroutine that generates random numbers asynchronously.

The `async_generator` coroutine defined in this module yields random float
values in
the range [0, 10) asynchronously. It uses the `asyncio.sleep` function to
introduce
a 1 second delay between each yield.

Example:
    ```
    import asyncio
    from async_generator import async_generator

    async def main():
        async for value in async_generator():
            print(value)

    asyncio.run(main())
    ```
"""

# imports
import asyncio
import random


async def async_generator():
    """
    Coroutine that generates random numbers.

    This coroutine loops 10 times, waiting for 1 second in each iteration
    before
    yielding a random float value in the range [0, 10).

    Yields:
        float: a random float value in the range [0, 10).

    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
