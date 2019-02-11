#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 20:56:51 2019

@author: donsdev
"""

def croper(length):
    global arr
    cnt = 0
    for elem in arr:
        cnt += elem // length
    return cnt
        
arr = [] 
n,target = map(int,input().split())
for _ in range(n):
    arr.append(int(input()))
start = 1
end = pow(2,31) 
while(start <= end):
    mid = (start + end) // 2
    if croper(mid) >= target:
        start = mid + 1
    else:
        end = mid - 1
print(end)