#!/usr/bin/env python3

import zipfile
import xml.etree.ElementTree as ET

class SampleList:
    def __init__(self):
        self.fname    = ""
        self.samples  = []
        self.vst      = []
        self.vsti     = []


def read_xrns(fname):
    xfile = ""
    with zipfile.ZipFile(fname) as xrns:
        with xrns.open('Song.xml') as song:
            xfile = song.read()

    root = ET.fromstring(xfile)
    sample_obj = SampleList()
    sample_obj.fname = fname

    for c in root[2].findall('Instrument'):
        # samples
        d = c.find('SampleGenerator').findall('Samples')
        for e in d:
            f = e.findall('Sample')
            sample_names = [g.find('Name').text for g in f]
            sample_obj.samples.append(sample_names)

        # vsti
        vsti = c.find('PluginGenerator').find('PluginDevice')
        if vsti:
            name = vsti.find('PluginDisplayName')
        print(vsti)

    return sample_obj


def main():
    # TODO parse cmd line
    fname = "test/cc.xrns"
    r = read_xrns(fname)
    pass

if __name__ == "__main__":
    main()
