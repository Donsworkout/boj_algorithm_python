#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 16:31:22 2019

@author: donsdev
"""

for _ in range(int(input())):
    arr = []
    for _ in range(int(input())):
        arr.append(list(map(int,input().split())))
    arr.sort()
    pin = arr[0][1];cnt = 0
    for elem in arr:
        if pin >= elem[1]:
            pin = elem[1]
            cnt += 1
        else:
            next       
    print(cnt)