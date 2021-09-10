#!/usr/bin/env python3

import zipfile
import hashlib
import xml.etree.ElementTree as ET
import argparse

class SampleList:
    def __init__(self):
        self.fname    = ""
        self.sample_name  = []
        self.sample_hash = []
        self.vst_name      = []
        self.vst_chunk      = []
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

def get_duplicate_samples(a, b):
    """
    return samples that are present in both a and b SampleList objects
    """
    results = []
    for i in range(len(a.sample_hash)):
        for j in range(len(b.sample_hash)):
            if a.sample_hash[i] == b.sample_hash[j]:
                match = (a.sample_name[i], b.sample_name[j])
                results.append(match)
    return results

def get_duplicate_vsti(a, b):
    """
    return vsti that are present in both a and b SampleList objects
    """
    results = []
    for i in range(len(a.vsti_chunk)):
        for j in range(len(b.vsti_chunk)):
            if a.vsti_chunk[i] == b.vsti_chunk[j]:
                match = (a.vsti_name[i], b.vsti_name[j])
                results.append(match)
    return results

def compare_files(sample_ls):
    if len(sample_ls) <= 1:
        print('Not enough files to compare')
        return
    
    def prin_res(duplicates, typ):
        if len(duplicates) == 0:
            print('No duplicate {} found'.format(typ))
        else:
            print('Duplicate {} found'.format(typ))
            for e in duplicates:
                print('Match:\n{}\n{}'.format(e[0], e[1]))

    for i in range(len(sample_ls) - 1):
        file_a = sample_ls[i]
        for j in range(i + 1, len(sample_ls)):
            file_b = sample_ls[j]
            dup_samp = get_duplicate_samples(file_a, file_b)
            dup_vsti = get_duplicate_vsti(file_a, file_b)

            print('Comparing {} {}'.format(file_a.fname, file_b.fname))

            prin_res(dup_samp, 'samples')
            prin_res(dup_vsti, 'vsti')


def main():
    parser = argparse.ArgumentParser(description='XRNS information tool.')
    parser.add_argument('file', 
            type=str, 
            nargs='+')
    parser.add_argument('--cmp', 
            dest='compare',
            help='Compare XRNS information between files.',
            action='store_true')
    args = parser.parse_args()

    # first get info for files
    sample_ls = []
    for f in args.file:
        r = read_xrns(f)
        sample_ls.append(r)

    #handle switches
    if args.compare:
        compare_files(sample_ls)
    else:
        for f in sample_ls:
            print(f.fname)
            print("===== Samples")
            print('\n'.join(f.sample_name))
            print("===== VSTI")
            print('\n'.join(f.vsti_name))
            print("===== VST")
            print('\n'.join(f.vst_name))

if __name__ == "__main__":
    main()
