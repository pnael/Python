#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__=="__main__":
    house_cost = int(input("House cost ?"))
    has_good_credit= False

    if house_cost >= 1000000:
        if has_good_credit:
            print("You need to pay "+str(house_cost*0.1))
        else:
            print("You need to pay "+str(house_cost*0.2))
    else:
        print("You need to pay "+str(house_cost *.10))
