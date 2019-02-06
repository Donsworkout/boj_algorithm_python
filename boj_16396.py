#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 13:47:31 2019

@author: donsdev
"""
#문제 풀이 중 입니다 (홍대 c)
"""
arr = [-1]*10001
for _ in range(int(input())):
    x, y = map(int,input().split())
    for i in range(x,y):
        arr[i] = True
cnt = 0
for elem in arr:
    if elem == True:
        cnt += 1
print(cnt)
"""