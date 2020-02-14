#!/usr/bin/python

import sys
import hashlib

file_path = sys.argv[0]
with open(file_path, 'rb') as file_handle:
    file_contents = file_handle.read()
    print('MD5 - ' + hashlib.md5(file_contents).hexdigest())
