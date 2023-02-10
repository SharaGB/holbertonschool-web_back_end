#!/usr/bin/env python3
""" Asyncio comprehension"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Return an async comprehension list """
    return [i async for i in async_generator()]
