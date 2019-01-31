#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 01:05:36 2019

@author: donsdev
"""
p=[]
d=[0]*10001
            
n,k = map(int,input().split())
for _ in range(n):
    p.append(int(input()))
d[0] = 1
for e in p:
    for i in range(e,k+1):
        d[i] += d[i-e]
print(d[k])