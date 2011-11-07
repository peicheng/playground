#!/usr/bin/env python
import bitarray

def prime_sum(n):
    psum = 0
    a = bitarray.bitarray(4000001)
    a.setall(1)
    count = 0
    for i in xrange(2, a.length()):
        if a[i] == True:
            print i
            if i > n:
                return psum
            psum += i
            for j in xrange(i * 2, a.length(), i):
                a[j] = False

if __name__ == '__main__':
    print prime_sum(2000000)
