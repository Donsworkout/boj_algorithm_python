#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 17:59:39 2019

@author: donsdev
"""
count = 0  
def z_move(n,x,y):
    global count
    if x == r and y == c:
        print(count)
        return
    if (x <= r and r < x + n) and (y <= c and c < y + n):
        z_move(n/2, x, y)
        z_move(n/2, x, y + n/2)
        z_move(n/2, x + n/2, y) 
        z_move(n/2, x + n/2, y + n/2) 
    else:
        count += int(n * n)
        return
        
N,r,c = map(int,input().split())
z_move(2**N,0,0)
