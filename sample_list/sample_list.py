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

    # vsti
    for c in root[2].findall('Instrument'):
        # vsti
        vsti = c.find('PluginGenerator').find('PluginDevice')
        if vsti:
            name = vsti.find('PluginDisplayName').text
            chunk = vsti.find('ParameterChunk').text
            oo = (name,chunk)
            sample_obj.vsti.append(oo)

    # samples taken from zip itself to calculate hashes
    with zipfile.ZipFile(fname) as xrns:
        for f in xrns.filelist[1:]:
            samp_name = f.filename()

    return sample_obj


def main():
    # TODO parse cmd line
    fname = "test/tester.xrns"
    r = read_xrns(fname)
    print(r.samples)
    pass

if __name__ == "__main__":
    main()
