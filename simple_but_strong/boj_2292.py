#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 16:03:56 2019

@author: donsdev
"""

n = int(input())
s = 1
i = 1
while(1):
    if n <= s + 6*(i-1):
        print(i)
        break
    s = s + 6*(i-1)
    i+=1