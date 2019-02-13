#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 16:48:16 2019

@author: donsdev
import sys
input = sys.stdin.readline
"""

def low(num):
    cnt = 0
    for i in range(1,n+1):
        cnt += min(n, mid // i)
    return cnt

n, k= int(input()), int(input())
left, right = 1, min(pow(10,9),n*n)

while left <= right:
    mid = (left + right) >> 1
    if low(mid) >= k:
        right = mid - 1
        ans = mid
    else:
        left = mid + 1
print(ans)
    

                
        