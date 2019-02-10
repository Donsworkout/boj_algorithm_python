#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 12:03:37 2019

@author: donsdev
"""

A,X = int(input()),int(input())
A_arr = [A]
r_bin_X = bin(X)[::-1]
exp = 2
while exp < X:
    A_arr.append((A_arr[-1]%1000000007)*(A_arr[-1]%1000000007))
    exp = exp * 2
t = 1
i = 0
for idx,elem in enumerate(r_bin_X):
    if elem == 'b':
        break
    else:
        if elem == '1':
              t = (t%1000000007) * (A_arr[idx]%1000000007)     
print(t%1000000007)