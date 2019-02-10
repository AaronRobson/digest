#!/usr/bin/python

import unittest

from isbn import check


class TestISBN(unittest.TestCase):

    def test(self):
        self.assertTrue(check('ISBN 0-596-00281-5'))
        self.assertEqual(check('ISBN 0-596-00281-', giveChecksum=True), 5)

        self.assertTrue(check('978-0-306-40615-7'))
        self.assertEqual(check('978-0-306-40615-', giveChecksum=True), 7)

        self.assertTrue(check('1903397-26-x'))
        self.assertEqual(check('1903397-26-', giveChecksum=True), 'X')

        self.assertTrue(check('0-313-20060-2'))
        self.assertEqual(check('0-313-20060-', giveChecksum=True), 2)
