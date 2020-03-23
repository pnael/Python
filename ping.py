#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

for i in range(254):
    ip = f'192.168.1.{i}'
    response = os.system("ping -c 1 " + ip+">/dev/null 2>&1")
    if response == 0:
        print(ip, 'is up!')