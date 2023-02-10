#!/usr/bin/env python3
""" Type-annotated function """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Type-annotated function make_multiplier that takes a float multiplier
        as argument and returns a function that multiplies a float by
        multiplier.
    """
    def func_multiplies(n: float) -> float:
        """ Type-annotated function func_multiplies that takes a float n as
            argument and returns the product of n and multiplier.
        """
        return n * multiplier
    return func_multiplies
