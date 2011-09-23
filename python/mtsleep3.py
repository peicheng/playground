#!/usr/bin/env python

import threading
from time import ctime, sleep

loops = [4, 2]

def loop(nloop, nsec):
    print 'start loop', nloop, 'at:', ctime()
    sleep(nsec)
    print 'loop', nloop, 'done at:', ctime()


def main():
    pass


if __name__ == '__main__':
    main()
