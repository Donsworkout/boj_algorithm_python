#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 22:58:18 2019

@author: donsdev
"""

cnt = 0
for j in range(8):
    s = ''
    inp = input()
    if j % 2 == 0:
        i = 0
        while i <= 6:
            s += inp[i]
            i += 2
    else:
        i = 1
        while i <= 7:
            s += inp[i]
            i += 2       
    s = s.replace('.','',4)
    cnt += len(s)
print(cnt)