#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 20:38:28 2019

@author: donsdev
"""

n = int(input())
d = [[]]*100001
d[0] = [1,1,1]
for i in range(1,n+1):
    d[i]= [(d[i-1][0] + d[i-1][1] + d[i-1][2])%9901, (d[i-1][0] + d[i-1][2])%9901, (d[i-1][0] + d[i-1][1])%9901]
print(sum(d[n-1])%9901)