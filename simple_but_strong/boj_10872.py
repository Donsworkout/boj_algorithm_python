#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 23:36:30 2019

@author: donsdev
"""

n = int(input())
l = n
if l == 0 or l == 1:
    print(1)
else:
    while(n > 1):
        l = l * (n - 1)
        n -= 1
    print(l)