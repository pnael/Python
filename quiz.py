#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, math

try:
        a = {"key": "value"}
        print("Success")
except:
        print("Failure")

try:
        b["key"] = "value"
        print("Success")
except:
        print("Failure")

try:
        c = {}
        c["key1"]["key2"] = "value"
        print("Success")
except:
        print("Failure")
                        
