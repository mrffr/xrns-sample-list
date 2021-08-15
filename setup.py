#!/usr/bin/env python3

import setuptools

with open("README.md",'r') as fh:
    long_description = fh.read()

setuptools.setup(
        name='',
        version='',
        description='',
        long_description=long_description,
        long_description_content_type="text/markdown",
        author='F Fitzgerald',
        url='https://github.com/mrffr/xrns-sample-list',

        entry_points={
            'console_scripts': [
                'xrns-sample-list = xrns-sample-list.sample_list:main',
                ],
            },

        packages=['xrns-sample-list'],
        classifie
        )
