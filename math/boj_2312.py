#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 22:36:50 2019

@author: donsdev
"""
def printer(arr):
    a = []
    for e in arr:
        if e not in a:
            print(str(e) + " " + str(arr.count(e)))
            a.append(e)
        
n = int(input())
for _ in range(n):
    arr = []
    num = int(input()) 
    while num != 1:
        i = 2
        while 1:
            if num % i == 0:
                num = int(num / i)
                arr.append(i)
                break
            i += 1
    printer(arr)