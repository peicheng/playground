#!/usr/bin/env python

import gzip, bz2

def genOpen(filenames):
    for name in filenames:
        if name.endswith('.gz'):
            yield gzip.open(name)
        elif name.endswith('bz2'):
            yield bz2.BZ2File(name)
        else:
            yield open(name)
