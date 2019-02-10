#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 17:28:27 2019

@author: donsdev
"""

def bsearch(start,end,target):
    if start > end:
        return 0
    mid = (start + end) // 2
    if target == A[mid]:
        return 1
    elif target < A[mid]:
        return bsearch(start,mid-1,target)
    else:
        return bsearch(mid+1,end,target)
    
n = int(input())
A = list(map(int,input().split()))
A.sort()
m = int(input())
B = list(map(int,input().split()))
for elem in B:
    print(bsearch(0,n-1,elem))