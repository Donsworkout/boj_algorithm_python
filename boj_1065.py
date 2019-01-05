#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 14:14:54 2019

@author: donsdev
"""

N = int(input())
C = 99
if N < 111:
    print(min(N,99))
else:
    for i in range(111,N+1):
        i = str(i)
        if int(i[2]) - int(i[1]) == int(i[1]) - int(i[0]):
            C += 1
    print(C)
            
