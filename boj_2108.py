#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 22:08:30 2019

@author: donsdev
import sys
input = sys.stdin.readline
"""

arr = []
n = int(input())
for _ in range(n):
    arr.append(int(input()))
arr.sort()

max_cnt = 0
max_idx = []
tmp = None
cnt = -1
for idx,elem in enumerate(arr):
    if tmp == elem:
        cnt += 1
    else:
        if cnt > max_cnt:
            max_idx = []
            max_idx.append(arr[idx-1])
            max_cnt = cnt
        elif cnt == max_cnt:
            max_idx.append(arr[idx-1])   
        cnt = 0
        tmp = elem
    if idx == len(arr) - 1:
        if cnt > max_cnt:
            max_idx = []
            max_idx.append(arr[idx])
        elif cnt == max_cnt:
            max_idx.append(arr[idx])

if len(max_idx) == 1:
    freq = max_idx[0]
else:
    freq = max_idx[1]
    
print(round(sum(arr)/n))
print(arr[int((n-1)/2)])
print(freq)
print(max(arr)-min(arr))