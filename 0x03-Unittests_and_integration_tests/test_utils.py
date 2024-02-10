#!/usr/bin/env python3
"""
Testing the utils module.
"""
import unittest
from parameterized import parameterized
from typing import Dict, List, Union
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Testing the access nested map method"""
    @parameterized.expand([
        ({"a": {"b": {"c": 1}}}, ["a", "b", "c"], 1),
        ({"x": {"y": {"z": 42}}}, ["x", "y", "z"], 42),
        ({"key1": {"key2": "value"}}, ["key1", "key2"], "value"),
    ])
    def test_access_nested_map(self, nested_map: Dict, path: List,
                               expected_result: Union[Dict, int]
                               ) -> None:
        """
        testing the method
        """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)
