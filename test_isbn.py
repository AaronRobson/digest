#!/usr/bin/python

import unittest

import isbn


class TestISBN(unittest.TestCase):

  def test(self):
    self.assertTrue(isbn.IsbnCheck('ISBN 0-596-00281-5'))
    self.assertEqual(isbn.IsbnCheck('ISBN 0-596-00281-', giveChecksum=True), 5)

    self.assertTrue(isbn.IsbnCheck('978-0-306-40615-7'))
    self.assertEqual(isbn.IsbnCheck('978-0-306-40615-', giveChecksum=True), 7)

    self.assertTrue(isbn.IsbnCheck('1903397-26-x'))
    self.assertEqual(isbn.IsbnCheck('1903397-26-', giveChecksum=True), 'X')

    self.assertTrue(isbn.IsbnCheck('0-313-20060-2'))
    self.assertEqual(isbn.IsbnCheck('0-313-20060-', giveChecksum=True), 2)


if __name__ == "__main__":
  unittest.main()
