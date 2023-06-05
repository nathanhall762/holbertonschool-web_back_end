#!/usr/bin/env python3
import unittest
from unittest.mock import patch, MagicMock, call
from functools import wraps
from utils import memoize


class TestMemoize(unittest.TestCase):

    class TestClass:
        def a_method(self):
            return 42

        @memoize
        def a_property(self):
            return self.a_method()

    def test_memoize(self):
        test_obj = self.TestClass()

        with patch.object(test_obj, 'a_method') as mock_method:
            result1 = test_obj.a_property()
            result2 = test_obj.a_property()

            mock_method.assert_called_once()
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
