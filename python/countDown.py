#!/usr/bin/env python

class countDown(object):
    def __init__(self, start):
        self.count = start
    def __iter__(self):
        return self
    def next(self):
        if self.count <= 10:
            raise StopIteration
        r = self.count
        self.count -= 1
        return r

if __name__ == '__main__':
    print 'hello world'
