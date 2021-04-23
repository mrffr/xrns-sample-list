#!/usr/bin/env python3

import zipfile
import xml.etree.ElementTree as ET

class SampleList:
    def __init__(self):
        fname    = ""
        samples  = []
        vst      = []
        vsti     = []
        

def read_xrns(fname):
    xfile = ""
    with zipfile.ZipFile(fname) as xrns:
        with xrns.open('Song.xml') as song:
            xfile = song.read()

    root = ET.fromstring(xfile)
    sample_obj = SampleList()

    for c in root:
        print(c.tag)


def main():
    fname = "test/tester.xrns"
    read_xrns(fname)

if __name__ == "__main__":
    main()
