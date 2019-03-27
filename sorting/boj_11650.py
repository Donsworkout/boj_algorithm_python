#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 00:08:05 2019

@author: donsdev
"""
import sys
input = sys.stdin.readline

arr = []
n = int(input())

for _ in range(n):
    a,b = map(int,input().split())
    arr.append((a,b))
    
for tup in sorted(arr):
    print(str(tup[0]) + " " + str(tup[1]))
