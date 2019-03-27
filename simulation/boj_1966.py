#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 19:07:24 2019

@author: donsdev
"""
#import sys
#input = sys.stdin.readline

def is_powerful(me,arr):
    for elem in arr:
        if elem[1] > me[1]:
            return 1
    return 0

p = int(input())
for _ in range(p):
    cnt = 0
    n,m = map(int, input().split())
    arr = [] 
    i = n 
    tmp = list(map(int, input().split()))
    tmp.reverse()
    while i > 0:
        if i - 1 == m:
            arr.append((1,tmp[n-i]))
        else:
            arr.append((0,tmp[n-i]))
        i -= 1
    j = n
    while(arr):
        if is_powerful(arr[-1],arr):
            arr.insert(0,arr.pop())
        else :
            cnt += 1
            if arr.pop()[0]:
                print(cnt)
                break 
