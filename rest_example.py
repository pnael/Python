#/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests

def get_answer(url):
    r = requests.get(url)
    return(r)

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
             raise ValueError('invalid user response')
        print(reminder)

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/todos/1'
    a = get_answer(url)
    print(a.json())
    print(type(a.json()))
    
