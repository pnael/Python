#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tkinter
from scapy.all import *
'''
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument(dest="entier", type=int,
                            help="entier d'entrée")
input_args = parser.parse_args()
entier = input_args.entier
'''

def arp_scan(ip):

    request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip)

    ans, unans = srp(request, timeout=2, retry=1)
    result = []

    for sent, received in ans:
        result.append({'IP': received.psrc, 'MAC': received.hwsrc})

    return result

def main():
    """ Main program """
    result = arp_scan("192.168.1.0/24")
    print(result)
    window = tkinter.Tk()
    greeting = tkinter.Text(result)
    greeting.pack()
    window.mainloop()
    return 0

if __name__ == "__main__":
    main()
