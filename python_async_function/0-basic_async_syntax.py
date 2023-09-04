#!/usr/bin/env python3
"""Write an asynchronous coroutine that takes
in an integer argument (max_delay, with a default value of 10)
named wait_random that waits for a random delay
between 0 and max_delay (included and float value)
seconds and eventually returns it.

Use the random module."""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Returns:
        Generator[float, None, None]: [description]
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


async def main():
    """
    Returns:
        [type]: [description]
    """
    async for i in async_generator():
        print(i)

if __name__ == "__main__":
    asyncio.run(main())
