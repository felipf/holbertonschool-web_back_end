#!/usr/bin/env python3
"""Import wait_random from the previous
python file that you have written
and write an async routine called wait_n that
takes in 2 int arguments (in this order): n
and max_delay. You will spawn wait_random n
times with the specified max_delay.

wait_n should return the list of all the delays
(float values). The list of the delays should be
in ascending order without using sort() because of concurrency."""
import asyncio
import random
from typing import List


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay between 0 and max_delay seconds"""
    i = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i


async def wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """spawn wait_random n times with the specified max_delay"""
    tasks = []
    delays = []
    for _ in range(n):
        tasks.append(wait_random(max_delay))
    for task in asyncio.as_completed(tasks):
        delays.append(await task)
    return delays


if __name__ == "__main__":
    asyncio.run(wait_n())
