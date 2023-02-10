#!/usr/bin/env python3
""" Type-annotated function """

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Type-annotated function element_length that takes a list lst as
        argument and returns a list of tuples (i, length) where i is the
        item and length is the length of the item.
    """
    return [(i, len(i)) for i in lst]
