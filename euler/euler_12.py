#!/usr/bin/env python
from collections import defaultdict

def ndiv(n, pfs):
    pows = defaultdict(int)
    
    for prime in pfs:
        while n % prime == 0:
            pows[prime] += 1
            n /= prime
    return reduce(lambda x, y : x * y, map(lambda x : x + 1, pows.values()))
    
def factors_gen():
    d = {}
    p = 2

    while True:
        if p not in d:
            d[p + p] = [p]
            yield p, [p]
        else:
            for i in d[p]:
                d.setdefault(i + p, []).append(i)
            yield p, d[p]
            del d[p]

        p += 1


def f(no):
    ndivs = {}
    ndivs[0] = 0
    ndivs[1] = 1
    for n,pfs in factors_gen():
        ndivs[n] = ndiv(n, pfs)
        even, odd = ((n - 1)//2, n) if n % 2 != 0 else (n // 2, n - 1)
        if ndivs[even] * ndivs[odd] >= no:
            print even * odd
            return 0

if __name__ == '__main__':
    f(500)
