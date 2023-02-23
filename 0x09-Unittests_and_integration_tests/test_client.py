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
    def test_org(self, url, payload):
        """ Test that the function returns the expected output """
        self.assertEqual(GithubOrgClient(url).org, payload.return_value)
        payload.assert_called_once()
