#!/usr/bin/env python3

import unittest
from sample_list import sample_list as sl

class TestSampleList(unittest.TestCase):
    def test_pass(self):
        self.assertEqual(1, 1)

    def test_read_empty_xrns_file(self):
        ll = sl.read_xrns("test/cc.xrns")
        self.assertEqual(ll.fname, "test/cc.xrns")
        self.assertEqual(len(ll.sample_name), 0)
        self.assertEqual(len(ll.vsti_name), 0)
        self.assertEqual(len(ll.vst_name), 0)

    def test_read_xrns_file(self):
        ll = sl.read_xrns("test/tester.xrns")
        self.assertEqual(ll.fname, "test/tester.xrns")
        self.assertEqual(len(ll.sample_name), 4)
        self.assertEqual(len(ll.vsti_name), 2)
        self.assertEqual(len(ll.vst_name), 0)

    def test_duplicate_samples_present(self):
        ll = sl.read_xrns("test/tester.xrns")
        lp = sl.read_xrns("test/tester.xrns")
        dups = sl.get_duplicate_samples(ll, lp)
        self.assertEqual(len(dups), 4)

    def test_duplicate_samples_not_present(self):
        ll = sl.read_xrns("test/cc.xrns")
        lp = sl.read_xrns("test/tester.xrns")
        dups = sl.get_duplicate_samples(ll, lp)
        self.assertEqual(len(dups), 0)

    def test_duplicate_vsti_present(self):
        ll = sl.read_xrns("test/tester.xrns")
        lp = sl.read_xrns("test/tester.xrns")
        dups = sl.get_duplicate_vsti(ll, lp)
        self.assertEqual(len(dups), 2)

    def test_duplicate_vsti_not_present(self):
        ll = sl.read_xrns("test/cc.xrns")
        lp = sl.read_xrns("test/tester.xrns")
        dups = sl.get_duplicate_vsti(ll, lp)
        self.assertEqual(len(dups), 0)

    def test_duplicate_vst_present(self):
        ll = sl.read_xrns("test/vst_test.xrns")
        lp = sl.read_xrns("test/vst_test.xrns")
        dups = sl.get_duplicate_vst(ll, lp)
        self.assertEqual(len(dups), 3)

    def test_duplicate_vst_not_present(self):
        ll = sl.read_xrns("test/cc.xrns")
        lp = sl.read_xrns("test/vst_test.xrns")
        dups = sl.get_duplicate_vst(ll, lp)
        self.assertEqual(len(dups), 0)

    def test_filter_samples(self):
        ll = sl.read_xrns("test/tester.xrns", ["samples"])
        self.assertEqual(len(ll.sample_name), 4)
        self.assertEqual(len(ll.vst_name), 0)
        self.assertEqual(len(ll.vsti_name), 0)

    def test_filter_vsti(self):
        ll = sl.read_xrns("test/tester.xrns", ["vsti"])
        self.assertEqual(len(ll.sample_name), 0)
        self.assertEqual(len(ll.vst_name), 0)
        self.assertEqual(len(ll.vsti_name), 2)

    def test_filter_vst_vsti(self):
        ll = sl.read_xrns("test/vst_test.xrns", ["vsti","vst"])
        self.assertEqual(len(ll.sample_name), 0)
        self.assertEqual(len(ll.vst_name), 3)
        self.assertEqual(len(ll.vsti_name), 2)



if __name__ == "__main__":
    unittest.main()
