#!/usr/bin/env python3

import unittest
from sample_list import sample_list as sl

class TestSampleList(unittest.TestCase):
    def test_pass(self):
        self.assertEqual(1, 1)

    def test_read_xrns_not_file(self):
        self.assertEqual(sl.read_xrns("NOTAFILE.xrns"), [])

    def test_read_xrns_file(self):
        self.assertEqual(sl.read_xrns("test/test.xrns"), [])


if __name__ == "__main__":
    unittest.main()
