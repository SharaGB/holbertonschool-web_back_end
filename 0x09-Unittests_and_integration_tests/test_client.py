#!/usr/bin/env python3
""" Test Github Org Client """
import unittest
from typing import Mapping, Sequence
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
from unittest import mock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    test github org client class
    """

    @parameterized.expand([("google"), ("abc")])
    @patch('client.get_json')
    def test_org(self, url, payload):
        """test org class"""
        self.assertEqual(GithubOrgClient(url).org, payload.return_value)
        payload.assert_called_once()


if __name__ == '__main__':
    unittest.main()
