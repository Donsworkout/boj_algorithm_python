#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 17:38:39 2019

@author: donsdev
"""

def process(upper):
    amt = 0
    for elem in arr:
        amt += min(upper,elem)
    return amt 

N = int(input())
arr = list(map(int,input().split()))
M = int(input())

if sum(arr) <= M:
    print(max(arr))
else:
    start,end = 1,max(arr)
    while(start <= end):
        mid = (start + end) >> 1
        if process(mid) > M:
            end = mid - 1
            ans = end
        elif process(mid) == M:
            ans = mid
            break
        else:
            start = mid + 1
    print(ans)