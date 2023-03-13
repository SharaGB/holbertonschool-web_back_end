#!/usr/bin/env python3
"""
Cache web module
"""

import redis
import requests
from functools import wraps
from typing import Callable

rd = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """ Count how many times a request has been made """

    @wraps(method)
    def wrapper(url):
        """ Wrapper for decorator """
        rd.incr(f"count:{url}")
        cached_html = rd.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode('utf-8')

        html = method(url)
        rd.setex(f"cached:{url}", 10, html)
        return html

    return wrapper


@count_requests
def get_page(url: str) -> str:
    """ Obtain the HTML content and returns it """
    req = requests.get(url)
    return req.text
