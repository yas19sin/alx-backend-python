#!/usr/bin/env python3
"""
Module for async_comprehension coroutine.
"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using an async comprehension
    over async_generator.
    """
    return [i async for i in async_generator()]
