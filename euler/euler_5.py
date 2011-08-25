#!/usr/bin/env python

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def gcd_m(l):
    return reduce(gcd, l)

if __name__ == '__main__':
    print gcd_m(range(1, 10))
