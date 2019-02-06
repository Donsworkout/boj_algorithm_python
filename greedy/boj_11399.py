#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 22:37:22 2019

@author: donsdev
"""

n = int(input())
arr = list(map(int,input().split()))
arr.sort()
amt = 0
tot = 0
for e in arr:
    amt += e
    tot += amt
print(tot)