#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 22:28:30 2019

@author: donsdev
"""

arr = []
sub = []
n = int(input())
while n > 0:
    arr.append(n)
    n-=1
while len(arr) + len(sub) > 1:
    while len(arr) > 1:
        arr.pop()
        sub.append(arr.pop())
    arr = sub[::-1] + arr
    sub = []
print(arr[0])