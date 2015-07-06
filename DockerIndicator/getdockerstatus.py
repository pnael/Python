#!/usr/bin/python

from subprocess import check_output
c = check_output(["docker", "ps"])

tab = c.split("\n");
print tab

