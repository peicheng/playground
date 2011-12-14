#!/usr/bin/env python


def carry(l):
    for i in range(len(l) - 1):
        l[i + 1] += l[i] / 10
        l[i] = l[i] % 10
    if l[-1] >= 10:
        tmp = l[-1] /10
        l[-1] = l[-1] %10
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

    carry(map(f, ia, ib))
    
def main():
    pass

if __name__ == '__main__':
    main()
