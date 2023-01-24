#!/usr/bin/env python3

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    """[summary]

    Args:
        n ([type]): [description]
        max_delay ([type]): [description]

    Returns:
        [type]: [description]
    """
    delays = []
    for i in range(n):
        delays.append(wait_random(max_delay))
    return [await delay for delay in asyncio.as_completed(delays)]
