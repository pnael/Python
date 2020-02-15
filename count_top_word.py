#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import sys

if __name__=="__main__":

    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        sys.stderr.write("Need a text filename\n")
        sys.exit(1)
        
    nbmots={}
    
    # Ouverture du fichier
    try:
        file = open(filename, 'r')

    except FileNotFoundError:
            sys.stderr.write(filename + " not found\n")
            sys.exit(1)
        
    lines = file.readlines()

    #Lecture ligne par ligne
    for line in lines:
        mots = line.split()
        for mot in mots:
            #on vire tout ce qui n'est pas alphanumerique
            mot = re.sub(r'\W+', '', mot.lower())
            if (mot in nbmots):
                nbmots[mot] = nbmots[mot] + 1
            else:
                nbmots[mot] = 1

    # on imprime les 30 mots les plus utilisés
    for i in range(0,30):
        max = 0
        for k,v in nbmots.items():
            if v > max:
                max = v
                mot = k
        del nbmots[mot]
        print(mot,max)
    
    
