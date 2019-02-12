#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 10:34:48 2019

@author: donsdev
import sys
input = sys.stdin.readline
"""

def cropped(su):
    length = 0
    for e in A:
        if e > su:
            length += e - su
    return length

N,M = map(int,input().split())
A = list(map(int,input().split()))

start = 0
end = max(A)
while start <= end:
    mid = (start + end) >> 1
    if cropped(mid) >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)