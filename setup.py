#!/usr/bin/env python3

import setuptools

with open("README.md",'r') as fh:
    long_description = fh.read()

setuptools.setup(
        name='xrns-sample-list-mrffr',
        version='0.0.1',
        description='CLI utility to list samples/vsti used in xrns files and to compare and detect duplicates between xrns files.',
        long_description=long_description,
        long_description_content_type="text/markdown",
        author='F Fitzgerald',
        url='https://github.com/mrffr/xrns-sample-list',
        license="MIT",

        entry_points={
            'console_scripts': [
                'xrns-sample-list = sample_list.sample_list:main',
                ],
            },

        packages=['sample_list'],
        classifiers=[
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3',
            ],
    )
