#!/usr/bin/env python3
"""
This module defines an asynchronous coroutine 'wait_random' that waits for a
random delay and returns it. The delay is a random float value between 0 and
a specified maximum delay.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and
    max_delay (inclusive, float value) seconds and eventually returns
    the delay.

    Args:
        max_delay (int): The upper bound for the random delay. Defaults to 10.

    Returns:
        float: The actual random delay time waited.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
