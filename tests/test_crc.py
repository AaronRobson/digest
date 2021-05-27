#!/usr/bin/python

import unittest

import crc


class TestCRC(unittest.TestCase):

    def test_crc32(self):
        self.assertEqual(hex(crc.get_crc32(b'hello-world')), hex(0xb1d4025b))
