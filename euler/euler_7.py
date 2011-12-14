#!/usr/bin/env python
import bitarray

def prime(n):
    a = bitarray.bitarray(10000000)
    a.setall(1)
    count = 0
    for i in xrange(2, a.length()):
        if a[i] == True:
            count += 1
            if count == n:
                return i
            for j in xrange(i * 2, a.length(), i):
                a[j] = False


if __name__ == '__main__':
    print prime(10001)
