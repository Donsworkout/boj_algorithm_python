#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 15:10:50 2019

@author: donsdev
"""
"""
def solve(n):
    global d
    if d.get(n):
        return d[n]
    else:
        min_val = 1000000
        if n % 3 == 0:
            min_val = min(min_val,solve(int(n/3)))
        if n % 2 == 0:
            min_val = min(min_val,solve(int(n/2)))     
        min_val = min(min_val, solve(n-1))
    d[n] = min_val + 1
    return d[n]
"""
n = int(input())
d = [0,0,1,1]
for i in range(4,n+1):
    d.append(d[i-1] + 1)
    if i % 2 == 0:
        d[i] = min(d[i], d[int(i/2)] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[int(i/3)] + 1)    
print(d[n])