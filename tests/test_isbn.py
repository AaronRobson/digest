#!/usr/bin/python

import unittest

from isbn import check


class TestCheck(unittest.TestCase):
    def test_isbn_prefix(self):
        self.assertTrue(check('ISBN 0-596-00281-5'))
        self.assertEqual(check('ISBN 0-596-00281-', giveChecksum=True), 5)

    def test_isbn_13(self):
        self.assertTrue(check('978-0-306-40615-7'))
        self.assertEqual(check('978-0-306-40615-', giveChecksum=True), 7)

    def test_isbn_10_x_checksum(self):
        self.assertTrue(check('1903397-26-x'))
        self.assertEqual(check('1903397-26-', giveChecksum=True), 'X')

    def test_isbn_10_numeric_checksum(self):
        self.assertTrue(check('0-313-20060-2'))
        self.assertEqual(check('0-313-20060-', giveChecksum=True), 2)

    def test_x_in_value(self):
        with self.assertRaises(ValueError):
            check('x987654321')

    def test_incorrect_length(self):
        with self.assertRaises(ValueError):
            check('4'*5)
