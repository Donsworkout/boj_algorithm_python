#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 21:37:38 2019

@author: donsdev
import sys 
input = sys.stdin.readline
"""

n = int(input())
arr = []
for _ in range(n):
    a,b = map(int,input().split())
    arr.append((b,a))
arr.sort()

cnt = 0
tmp = 0

for b,a in arr:
    if a >= tmp:
        tmp = b
        cnt += 1
print(cnt)

"""
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14
"""