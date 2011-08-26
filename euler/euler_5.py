#!/usr/bin/env python

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

if __name__ == '__main__':
    print reduce((lambda x, y: x * y/ gcd(x, y)), range(1,11))
