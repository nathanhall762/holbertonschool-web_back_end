#!/usr/bin/env python3
"""
This module defines a coroutine that measures the runtime of another coroutine.

The `measure_runtime` coroutine defined in this module takes no arguments and
executes the `async_comprehension` coroutine from a previous task four times in
parallel using `asyncio.gather()`. The total runtime of the four coroutines is
measured and returned.

Example:
    ```
    import asyncio
    from measure_runtime import measure_runtime

    async def main():
        runtime = await measure_runtime()
        print(f"Total runtime: {runtime:.2f} seconds")

    asyncio.run(main())
    ```
"""


import asyncio
from time import perf_counter
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in parallel using asyncio.gather
    and measures the total runtime.

    Returns:
        float: the total runtime in seconds.

    """
    start_time = perf_counter()

    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())

    end_time = perf_counter()

    return end_time - start_time
