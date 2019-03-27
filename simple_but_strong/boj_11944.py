#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 02:19:48 2019

@author: donsdev
"""

n,m = map(int,input().split())
s_n = str(n)
l = len(s_n)
if n*l < m:
    print(s_n * n)
else:
    print(s_n * int(m/l),end='')
    for i in range(m % l):
        print(s_n[i],end='')
