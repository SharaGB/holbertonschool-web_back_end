#!/usr/bin/env python3

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """[summary]

    Args:
        max_delay (int, optional): [description]. Defaults to 10.

    Returns:
        float: [description]
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
