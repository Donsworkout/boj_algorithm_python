#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 13:45:55 2019

@author: donsdev
"""
def possible(dist):
    cnt,i = 1,1
    start = house[0]
    while i <= N-1:
        if house[i] - start >= dist:
            cnt += 1
            start = house[i]
        i += 1
    if cnt >= C:
        return True
    else:
        return False
    
N,C = map(int,input().split())
house = []
for _ in range(N):
    house.append(int(input()))
house.sort()
left, right = 1, house[-1] - house[0]
while left <= right:
    mid = (left + right) >> 1
    if possible(mid):
        left = mid + 1
    else:
        right = mid - 1
print(right)