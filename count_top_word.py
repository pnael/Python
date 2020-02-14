#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re


if __name__=="__main__":
    filename = '135-0.txt'
    nbmots={}
    
    # Ouverture du fichier
    file = open(filename,'r')
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
    
    
