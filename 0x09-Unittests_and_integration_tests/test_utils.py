#!/usr/bin/env python3
""" Test cases for utils.py """
from parameterized import parameterized
import unittest
from utils import (access_nested_map, get_json, memoize)
from unittest import mock
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """ Class for Testing Access Nested Map """

    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ('a',), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Test that the function returns the expected output """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ('a',), 'a'),
        ({'a': 1}, ('a', 'b'), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """ Test that the function raises the expected exception """
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError('{expected}')", repr(e.exception))


class TestGetJson(unittest.TestCase):
    """ Class for Testing Get Json """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload):
        """ Test that the function returns the expected output """
        mock_response = mock.Mock()
        mock_response.json.return_value = payload

        with mock.patch('requests.get', return_value=mock_response):
            self.assertEqual(get_json(url), payload)
            mock_response.json.assert_called_once()


class TestMemoize(unittest.TestCase):
    """ Class for Testing Memoize """

    def test_memoize(self):
        """ Test that the function returns the expected output """
        class TestClass:
            """ Test Class """

            def a_method(self):
                """ Test Method """
                return 42

            @memoize
            def a_property(self):
                """ Test Property """
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock:
            test_class = TestClass()
            test_class.a_property()
            mock.assert_called_once()
