#!/usr/bin/env python

import os
import fnmatch

def genFind(pattern, top):
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, pattern):
            yield os.path.join(path, name)
            
if __name__ == "__main__":
    pyfiles = genFind('*.py', '/home/jxq/')
    for file in pyfiles:
        print file
