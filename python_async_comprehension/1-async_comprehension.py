#!/usr/bin/env python3
"""
This module defines a coroutine that collects 10 random numbers
using an async comprehension.

The `async_comprehension` coroutine defined in this module uses the
`async_generator` coroutine from the previous task to collect 10 random
float values asynchronously. It uses an async comprehension to simplify
the process of collecting the values.

Example:
    ```
    import asyncio
    from async_comprehension import async_comprehension

    async def main():
        result = await async_comprehension()
        print(result)

    asyncio.run(main())
    ```
"""

# imports
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using an async comprehension.

    This coroutine uses an async comprehension over the `async_generator`
    coroutine
    to collect 10 random float values asynchronously.

    Returns:
        List[float]: a list of 10 random float values.

    """
    return [value async for value in async_generator()][:10]
