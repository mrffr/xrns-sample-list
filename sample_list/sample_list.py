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

    for c in root[2].findall('Instrument'):
        d = c.find('SampleGenerator').findall('Samples')
        if len(d) > 0:
            for e in d:
                f = e.findall('Sample')
                print(f)



def main():
    fname = "test/tester.xrns"
    fname = "test/cc.xrns"
    read_xrns(fname)

if __name__ == "__main__":
    main()
