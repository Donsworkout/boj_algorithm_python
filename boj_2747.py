#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 22:41:26 2019

@author: donsdev
"""

def fibo(n):
    global cache
    if cache[n] != -1:
        return cache[n]
    else:
        cache[n] = fibo(n-2) + fibo(n-1)
        return cache[n] 
   
n = int(input())
cache = [-1] * (n + 1)
cache[0] = 0
cache[1] = 1
print(fibo(n))