#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 09:39:01 2019

@author: donsdev
import sys
input = sys.stdin.readline
"""

N,M = map(int,input().split())
pack = []
indi = []
for _ in range(M):
    p,i = map(int,input().split())
    pack.append(p)
    indi.append(i)
if N < 6:
    print(min(min(pack),N*min(indi)))
else:
    print(min((N//6 + 1) * min(pack),(N//6)*min(pack) + (N%6)*min(indi),N*min(indi)))