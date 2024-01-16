#!/usr/bin/env python3
"""
fifth task module
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    The code is nearly identical to wait_n except task_wait_random is
    being called. The funtion spawns task_wait_random (n) times with
    the specified max_delay.
    """
    tasks = []
    for i in range(n):
        tasks.append(task_wait_random(max_delay))
    return [await task for task in asyncio.as_completed(tasks)]
