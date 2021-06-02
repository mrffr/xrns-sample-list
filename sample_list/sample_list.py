#!/usr/bin/env python3

import zipfile
import hashlib
import xml.etree.ElementTree as ET

class SampleList:
    def __init__(self):
        self.fname    = ""
        self.sample_name  = []
        self.sample_hash = []
        self.vst      = []
        self.vsti_name     = []
        self.vsti_chunk     = []

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
            sample_obj.vsti_name.append(name)
            sample_obj.vsti_chunk.append(chunk)

    # samples taken from zip itself to calculate hashes
    with zipfile.ZipFile(fname) as xrns:
        for f in xrns.filelist[1:]:
            samp_name = f.filename
            # calc hash
            raw = xrns.open(f.filename)
            block_size = 65536
            hh = hashlib.sha256()
            fb = raw.read(block_size)
            while len(fb) > 0:
                hh.update(fb)
                fb = raw.read(block_size)
            digest = hh.hexdigest()

            # store info
            sample_obj.sample_name.append(samp_name)
            sample_obj.sample_hash.append(digest)


    return sample_obj


def main():
    # TODO parse cmd line
    fname = "test/tester.xrns"
    r = read_xrns(fname)
    print(r.samples)
    pass

if __name__ == "__main__":
    main()
