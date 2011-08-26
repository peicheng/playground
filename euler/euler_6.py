#!/usr/bin/env python

def sum_of_sqr(l):
    return sum(map((lambda x: x*x), l))

def sqr_of_sum(l):
    return sum(l) * sum(l)

if __name__ == '__main__':
    print sum_of_sqr(range(1, 101)) - sqr_of_sum(range(1, 101))
