#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 12:41:19 2019

@author: donsdev
"""

def painter(n,y,x):
    if n == 1:
        pan[y][x] = "*"
        return
    div = int(n/3)
    for i in range(0,3):
        for j in range(0,3):
            if i == 1 and j == 1: 
                pass
            else:
                painter(div, y + i*div, x + j*div)
    
n = int(input())
pan = [[' '] * n for i in range(n)]
painter(n,0,0)
for j in range(0,n):
    print(*pan[j])