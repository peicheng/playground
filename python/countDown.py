#!/usr/bin/env python

class countDown(object):
    def __init__(self, start):
        self.count = start
    def __iter__(self):
        return self
    def next(self):
        if self.count <= 0:
            raise StopIteration
        r = self.count
        self.count -= 1
        return r

def countDown2(n):
    print 'Counting down from', n
    while n > 0:
        yield n
        n -= 1
        
if __name__ == '__main__':
    c = countDown(5)
    for i in c:
        print i
    c = countDown2(10)
    for i in c:
        print i
