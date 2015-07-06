#!/usr/bin/python
# -*- coding: utf-8 -*-

the_count = [1,2,3,4,5]
fruits = ['apple','orange','pears','apricot']
change = [1, 'pennies',2,'dimes',3,'quarters']

#this first kind of loop goes through a list
for number in the_count:
    print("This is count %d" % number)

#same as above
for fruit in fruits:
    print("a fruit of type: %s" % fruit)

#also we an go to mixed list too
#notice we have to use %r since we don't what's in it
for i in change:
    print("I got %r" % i)

#We can also build list, first start with an empty one
elements = []

#then use the range() function to do 0 to 5 counts
for i in range(0,6):
    print("adding %d to the list" % i)
    #append is a function that list understand
    elements.append(i)

#now we can print them too
for i in elements:
    print("Element was: %d" % i)

