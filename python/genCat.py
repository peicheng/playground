#!/usr/bin/env python

def genCat(sources):
    for s in sources:
        for item in s:
            yield item
