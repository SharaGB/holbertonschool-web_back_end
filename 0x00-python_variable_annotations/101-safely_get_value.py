#!/usr/bin/env python3
""" Type-annotated function """

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')  # Declare type variable


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """ Type-annotated function safely_get_value that takes a dictionary dct,
        a key and a default value and returns the value in dct by key or the
        default value if the key doesn't exist.
    """
    if key in dct:
        return dct[key]
    else:
        return default
