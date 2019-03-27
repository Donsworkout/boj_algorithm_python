#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 23:19:24 2019

@author: donsdev
"""

def pado(n):
    global cache
    if cache[n] != -1:
        return cache[n]
    else:
        cache[n] = pado(n-3) + pado(n-2)
        return cache[n] 

c = int(input())
for _ in range(c):
    n = int(input())
    cache = [-1] * (n)
    if n < 3 :
        for i in range(n):
            cache[n-1] = 1
        print(cache[n-1])
    else:
        cache[0],cache[1],cache[2]= 1,1,1
        print(pado(n-1))