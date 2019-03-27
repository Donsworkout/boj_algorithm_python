#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 12:55:56 2019

@author: donsdev
"""

def tyle(n):
    global cache
    if d[n] != -1:
        return d[n]
    else:
        d[n] = (2 * tyle(n-2) + tyle(n-1)) % 10007
        return d[n]
n = int(input())
if n == 1:
    print(1)
else:
    d = cache = [-1] * (n + 1)
    d[1],d[2] = 1,3
    print(tyle(n))