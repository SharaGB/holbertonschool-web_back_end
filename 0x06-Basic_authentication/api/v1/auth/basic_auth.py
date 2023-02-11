#!/usr/bin/env python3
""" BasicAuth class module """
from api.v1.auth.auth import Auth
import base64
from typing import Tuple, TypeVar
from models.user import User


class BasicAuth(Auth):
    """ BasicAuth class
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """ Return the Base64 part of the Authorization header
            for a Basic Authentication
        """
        if authorization_header is None or \
                type(authorization_header) is not str or \
                authorization_header[:6] != 'Basic ':
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ Return the decoded value of a Base64 string
        """
        if base64_authorization_header is None or \
                type(base64_authorization_header) is not str:
            return None
        try:
            decode = base64.b64decode(base64_authorization_header)
            return decode.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """ Return the user email and password from the Base64 decoded value
        """
        if decoded_base64_authorization_header is None or \
                type(decoded_base64_authorization_header) is not str or \
                ':' not in decoded_base64_authorization_header:
            return None, None
        u_email, u_password = decoded_base64_authorization_header.split(':', 1)
        return u_email, u_password

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """ Return the User instance based on his email and password
        """
        if user_email is None or type(user_email) is not str or \
                user_pwd is None or type(user_pwd) is not str:
            return None
        try:
            users = User.search({'email': user_email})
        except Exception:
            return None
        for password in users:
            if password.is_valid_password(user_pwd):
                return password
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Overload Auth and retrieve the User instance for a request
        """
        auth_header = self.authorization_header(request)
        base64_header = self.extract_base64_authorization_header(auth_header)
        decode_header = self.decode_base64_authorization_header(base64_header)
        email, password = self.extract_user_credentials(decode_header)
        return self.user_object_from_credentials(email, password)
