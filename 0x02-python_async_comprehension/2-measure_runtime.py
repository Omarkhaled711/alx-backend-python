#!/usr/bin/env python3
"""
third task module
"""

from asyncio import gather
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    a measure_runtime coroutine that will execute async_comprehension
    four times in parallel using asyncio.gather.
    """
    start = time()
    coroutines = [async_comprehension() for _ in range(4)]
    await gather(*coroutines)
    return time() - start
