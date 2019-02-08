#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 18:12:18 2019

@author: donsdev
"""

def quad(size,x,y):
    if size == 1:
        print(arr[y][x],end='')
        return 
    same = True
    for i in range(y,y+size):
        for j in range(x,x+size):
            if arr[i][j] != arr[y][x]:
                same = False
    if same == True:
        print(arr[y][x],end='')
        return 
    offset = size // 2
    print('(',end='')
    quad(offset,x,y)
    quad(offset,x+offset,y)
    quad(offset,x,y+offset)
    quad(offset,x+offset,y+offset)
    print(')',end='')   
    
arr = []
n = int(input())
for _ in range(n):
    arr.append(input())
quad(n,0,0)