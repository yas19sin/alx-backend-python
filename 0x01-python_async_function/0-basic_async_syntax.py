#!/usr/bin/env python3
"""
Module with an asynchronous coroutine.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay seconds
    and eventually returns it.

    Args:
        max_delay (int): The maximum delay value (default is 10).

    Returns:
        float: The random delay waited.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
