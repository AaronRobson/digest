#!/usr/bin/python

import unittest

import crc


class TestCRC(unittest.TestCase):

    def testCRC32(self):
        self.assertEqual(hex(crc.GetCRC32(b'hello-world')), hex(0xb1d4025b))


if __name__ == "__main__":
    unittest.main()
