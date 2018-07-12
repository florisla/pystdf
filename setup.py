#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# PySTDF - The Pythonic STDF Parser
# Copyright (C) 2006 Casey Marshall
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import io
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command

NAME = 'pystdf'
DESCRIPTION = 'Python module for working with STDF files'
URL = 'https://github.com/cmars/pystdf'
EMAIL = 'casey.marshall@gmail.com'
AUTHOR = 'Casey Marshall'
REQUIRES_PYTHON = '>=3.4.0'
VERSION = None

REQUIRED = [
]

EXTRAS = {
    'dataframe': ['pandas'],
    'xlsx': ['pandas', 'openpyxl'],
}

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load __version__.py module as a dictionary.
about = {}
if not VERSION:
    with open(os.path.join(here, NAME, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['VERSION'] = VERSION


setup(
    name=NAME,
    version='.'.join(str(num) for num in about['VERSION']),
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    entry_points={
        'console_scripts': [
            'stdf2text=pystdf.script.totext:main',
            'stdf2excel=pystdf.script.toexcel:main',
            'stdf2xml=pystdf.script.toxml:main',
            'stdfcount=pystdf.script.count:main',
            'stdfslice=pystdf.script.slice:main',
        ],
    },
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    include_package_data=True,
    license='MIT',
    classifiers=[
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: Free for non-commercial use',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)'
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
        'Operating System :: OS Independent',
        'Intended Audience :: Manufacturing',
        'Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)

