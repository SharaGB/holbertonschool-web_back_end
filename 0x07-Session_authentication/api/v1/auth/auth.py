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
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        for excluded_path in excluded_paths:
            if excluded_path[-1] != '*':
                continue
            if path.startswith(excluded_path[:-1]):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Return the header value
        """
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """ Return the current user
        """
        return None
