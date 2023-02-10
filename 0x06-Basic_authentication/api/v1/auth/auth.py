#!/usr/bin/env python3
""" Auth class module """
from flask import request
from typing import List, TypeVar


class Auth():
    """ Auth class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Determine if the path is in the excluded paths
        """
        if excluded_paths is None or excluded_paths == []:
            return True
        for ex_path in excluded_paths:
            if ex_path == path:
                return False
            if ex_path.endswith('*'):
                pfx_path = ex_path[:-1]
                if pfx_path in path:
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Return the header value
        """
        if request is None or ("Authorization" not in request.headers):
            return None
        return request.headers["Authorization"]

    def current_user(self, request=None) -> TypeVar('User'):
        """ Return the current user
        """
        return None
