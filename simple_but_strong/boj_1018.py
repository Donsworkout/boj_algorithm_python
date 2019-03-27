#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 15:12:45 2019

@author: donsdev
"""
# 이차원 리스트 선언법 
row,col = map(int,input().split())
pan = [[0 for cols in range(col)]for rows in range(row)]
for i in range(0,row) :
    inputs = input()
    for j in range(0,col) :
        pan[i][j] = inputs[j]
min_val = 99999999
for x in range(0,row - 7):
    for y in range(0,col - 7):
        c_w, c_b = 0,0
        for i in range(x, x + 8):
            for j in range(y, y + 8):
                if (i % 2 == 0):
                    if ((j % 2 == 0) and (pan[i][j] == "B")) or ((j % 2 != 0) and (pan[i][j] == "W")):
                        c_w += 1
                    if ((j % 2 == 0) and (pan[i][j] == "W")) or ((j % 2 != 0) and (pan[i][j] == "B")):
                        c_b += 1
                else:
                    if ((j % 2 == 0) and (pan[i][j] == "W")) or ((j % 2 != 0) and (pan[i][j] == "B")):
                        c_w += 1  
                    if ((j % 2 == 0) and (pan[i][j] == "B")) or ((j % 2 != 0) and (pan[i][j] == "W")):
                        c_b += 1 
        min_val = min(min_val,min(c_w, c_b))
print(min_val)