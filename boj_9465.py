#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 22:29:11 2019

@author: donsdev
"""

T = int(input())
for _ in range(T):
    n = int(input())
    D = [[0,0,0]] + [[]] * n
    A = [list(map(int,input().split()))] + [list(map(int,input().split()))]
    i = 1
    while i <= n:
        D[i] = [max(D[i-1][0],D[i-1][1],D[i-1][2]), max(D[i-1][0],D[i-1][2])+A[0][i-1], max(D[i-1][0],D[i-1][1])+A[1][i-1]]
        i+=1
    print(max(D[n]))