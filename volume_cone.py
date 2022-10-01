#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


if __name__=="__main__":
    print("Volume d'un cône droit")
    r = int(input("Rayon du cône : "))
    h = int(input("Hauteur du cône : "))
    v = (1/3)*math.pi*r*r*h
    
    print("Volume du cône : ",v," m3")
