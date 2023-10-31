#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(ordered), 5)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [1, 2, 3, 5, 4]
        self.assertEqual(max_integer(unordered), 5)

    def test_max_at_begginning(self):
        """Test a list with a beginning max value."""
        max_at_beginning = [5, 4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 5)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        one_element = [9]
        self.assertEqual(max_integer(one_element), 9)

    def test_floats(self):
        """Test a list of floats."""
        floats = [2.53, 7.33, -10.123, 16.2, 7.0]
        self.assertEqual(max_integer(floats), 16.2)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [1.5, 19.51, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 19.51)

    def test_string(self):
        """Test a string."""
        string = "Chrisken"
        self.assertEqual(max_integer(string), 's')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Chrisken", "is", "my", "id"]
        self.assertEqual(max_integer(strings), "my")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
