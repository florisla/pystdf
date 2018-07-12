#!/usr/bin/env python
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
#

from __future__ import print_function
import sys
import re

try:
    import gzip
except ImportError:
    gzip = None
try:
    import bz2
except ImportError:
    bz2 = None

from pystdf.IO import Parser
from pystdf.Indexing import RecordIndexer


GZ_PATTERN = re.compile('\.g?z', re.I)
BZ2_PATTERN = re.compile('\.bz2', re.I)


def process_file(file_name):
    reopen_fn = None
    if file_name is None:
        f = sys.stdin
    elif GZ_PATTERN.search(file_name):
        if not gzip:
            print("gzip is not supported on this system", file=sys.stderr)
            sys.exit(1)
        reopen_fn = lambda: gzip.open(file_name, 'rb')
        f = reopen_fn()
    elif BZ2_PATTERN.search(file_name):
        if not bz2:
            print("bz2 is not supported on this system", file=sys.stderr)
            sys.exit(1)
        reopen_fn = lambda: bz2.BZ2File(file_name, 'rb')
        f = reopen_fn()
    else:
        f = open(file_name, 'rb')
    indexer = RecordIndexer()
    p = Parser(inp=f, reopen_fn=reopen_fn)
    p.addSink(indexer)
    p.parse()
    f.close()
    print("Record count: ", indexer.recid)


def main():
    if len(sys.argv) < 2:
        print("Usage: %s <stdf file>" % (sys.argv[0]))
    else:
        process_file(sys.argv[1])


if __name__ == "__main__":
    main()
