#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 01:12:40 2019

@author: donsdev
"""

s = []
for i in range(int(input())):
    n = int(input())
    if n != 0:
        s.append(n)
    else:
        s.pop()
print(sum(s))
        