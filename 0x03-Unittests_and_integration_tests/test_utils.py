#!/usr/bin/env python3
"""
Testing the utils module.
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from typing import Dict, Tuple, Union
from utils import (access_nested_map, get_json, memoize)


class TestAccessNestedMap(unittest.TestCase):
    """Testing the access nested map method"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Dict, path: Tuple[str],
                               expected_result: Union[Dict, int]
                               ) -> None:
        """
        testing the method without exceptions
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map: Dict,
                                         path: Tuple[str],
                                         exception: Exception,
                                         ) -> None:
        """
        Testing the exceptions raised by access nested map method.
        """
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Testing the get_json method.
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url: str, test_payload: Dict,
                      ) -> None:
        """
        testing the method
        """
        attrs = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**attrs)) as get_request:
            self.assertEqual(get_json(test_url), test_payload)
            get_request.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    Testing the memoize method
    """

    def test_memoize(self) -> None:
        """
        Testing the method ensuring that memoization works
        """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, "a_method") as memo:
            test_cls = TestClass()
            test_cls.a_property()
            test_cls.a_property()
            memo.assert_called_once()
