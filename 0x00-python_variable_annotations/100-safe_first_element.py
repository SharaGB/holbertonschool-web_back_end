#!/usr/bin/env python3
""" Type-annotated function """

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Type-annotated function safe_first_element that takes a list lst as
        argument and returns the first element of the list or None if the list
        is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
