#!/usr/bin/env python3
""" Test Github Org Client """
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized
from unittest.mock import patch
import unittest


class TestGithubOrgClient(unittest.TestCase):
    """ Class for Testing Github Org Client """

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, input, mock):
        """ Test that the function returns the expected output """
        test_class = GithubOrgClient(input)
        test_class.org()
        mock.assert_called_once_with(f'https://api.github.com/orgs/{input}')
