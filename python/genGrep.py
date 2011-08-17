#!/usr/bin/env python

import re

def genGrep(pattern, lines):
    patc = re.compile(pat)
    for line in lines:
        if patc.search(line):
            yield line
