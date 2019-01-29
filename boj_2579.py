#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 14:13:37 2019

@author: donsdev
"""

def get_sum(n):
    if d[n] != -1:
        return d[n]
    else:
        d[n] = max(get_sum(n-2) + val[n], get_sum(n-3) + val[n-1] + val[n])
        return(d[n])

n = int(input())
val = [0]
d = [-1] * (n+1)
for i in range(0,n+1):
    if i!=0:
        val.append(int(input()))
    if i==0 or i==1:
        d[i] = val[i]
    elif i==2:
        d[i] = d[1] + val[2]        

print(get_sum(n))