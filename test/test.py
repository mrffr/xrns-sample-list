#!/usr/bin/env python3

import unittest
from sample_list import sample_list as sl

class TestSampleList(unittest.TestCase):
    def test_pass(self):
        self.assertEqual(1, 1)

    def test_read_xrns_file(self):
        ll = sl.read_xrns("test/cc.xrns")
        self.assertEqual(ll.fname, "test/cc.xrns")
        self.assertEqual(ll.vsti, [])
        self.assertEqual(ll.vst, [])
        self.assertEqual(ll.samples, [])

    def test_read_xrns_file(self):
        ll = sl.read_xrns("test/tester.xrns")
        self.assertEqual(ll.fname, "test/tester.xrns")
        self.assertNotEqual(ll.samples, [])
        self.assertNotEqual(ll.vsti, [])
        self.assertEqual(ll.vst, [])

if __name__ == "__main__":
    unittest.main()
