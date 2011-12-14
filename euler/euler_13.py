#!/usr/bin/env python

def carry(l):
    tmp = 0
    for i in range(len(l) - 1):
        l[i + 1] += l[i] / 10
        l[i] = l[i] % 10
    if l[-1] >= 10:
        tmp = l[-1] /10
        l[-1] = l[-1] %10
    if tmp != 0:
        l.append(tmp)

    return l

def add(a, b):
    def f(x, y):
        if x == None:
            return y
        if y == None:
            return x
        return x + y

    ia = list(int(c) for c in a)
    ia.reverse()
    ib = list(int(c) for c in b)
    ib.reverse()

    res = carry(map(f, ia, ib))
    res.reverse()

    return res
    
def main():
    l = [line.rstrip() for line in open('/home/jxq/code/tmp')]
    print ''.join(map(str, reduce(add, l)[:10]))

if __name__ == '__main__':
    main()
