#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 21:21:15 2019

@author: donsdev

그리고 import sys 해서 입력 빠르게 rstrip() 까지
"""
import sys
input = sys.stdin.readline

arr = []
n = int(input())
for _ in range(n):
    arr.append(int(input()))
print(*sorted(arr),sep="\n")