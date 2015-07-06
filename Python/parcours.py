#! /usr/bin/env python
FILESROOT = '/home/nael/'
LINKSROOT = '/home/nael/'
import os, sys

def main():
    for d in os.walk(FILESROOT):
        for f in d[2]:
            do_file(os.path.join(d[0], f))

def do_file(f):
    print f

if __name__ == '__main__':
    main()
