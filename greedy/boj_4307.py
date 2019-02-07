#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 00:37:48 2019

@author: donsdev
"""

for _ in range(int(input())):
    l,c = map(int,input().split())
    arr = []
    for _ in range(c):
        arr.append(int(input()))
    med = l // 2
    min_v = med
    max_v = 0
    min_e = 0
    for elem in arr:
        if max(abs(l-elem),abs(0-elem)) > max_v:
            max_v = max(abs(l-elem),abs(0-elem)) 
        if abs(med-elem) < min_v:
            min_v = abs(med-elem)
            min_e = elem
    print(min(abs(0-min_e),abs(l-min_e)), max_v)