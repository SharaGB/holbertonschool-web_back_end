#!/usr/bin/env python3
""" Measure the runtime """

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """[summary]

    Args:
        n (int): [description]
        max_delay (int): [description]

    Returns:
        float: [description]
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    return (end - start) / n
