#!/usr/bin/python
# -*- coding: utf-8 -*-

digit=["","one","two","three","four","five","six","seven","eight","nine"]
excep_11=["","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
tens = ["","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]




if __name__=="__main__":

    for c in range(10):
        if c > 0:
            print digit[c],"hundred"
        for t in range(10):
            if t > 0 and c==0:
                print tens[t]
            elif t>0 :
                print digit[c],"hundred and",tens[t]
            for d in range(1,10):
                if c==0 and t==1 and d>0:
                    print excep_11[d]
                elif c==0:
                    print tens[t],digit[d] 
                elif c>0 and t==1 and d>0:
                    print digit[c],"hundred and",excep_11[d]
                else:
                    print digit[c],"hundred and",tens[t],digit[d] 
    print "one thousand"
