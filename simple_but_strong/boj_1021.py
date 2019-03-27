#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 15:26:30 2019

@author: donsdev
"""
#import sys
#input = sys.stdin.readline 

arr = []
cnt = 0
n,m = map(int,input().split())
for i in range(n):
    arr.append(i+1)
targets = list(map(int,input().split()))
targets.reverse()
while targets:
    if targets[-1] == arr[0]:
        targets.pop()
        arr.pop(0)
    else:
        if abs(arr.index(targets[-1]) - arr.index(arr[0])) <= abs(arr.index(targets[-1]) - arr.index(arr[-1])):
            cnt += 1
            arr.append(arr.pop(0))
        else:
            cnt += 1
            arr.insert(0,arr.pop())              
print(cnt)