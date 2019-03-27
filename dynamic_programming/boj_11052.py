#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 00:43:53 2019

@author: donsdev
"""
n = int(input())
A = [0]
A += list(map(int, input().split()))
d = [0]

for i in range(1,n+1):
    max_v = A[i]
    for j in range(1,i+1):
        if max_v < d[i-j] + A[j]:
            max_v = d[i-j] + A[j]
        j+=1
    d.append(max_v)              
    i+=1
print(d[n])