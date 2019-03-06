#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 15:26:00 2019

@author: donsdev
"""

dice = [0,0,0,0,0,0]
n,m,x,y,k = map(int,input().split())
pan = []
for _ in range(n):
    pan.append(list(map(int,input().split())))
moves = list(map(int,input().split()))
top = 0
for move in moves:
    if move == 1:
        a,b = x, y+1
        if (a > n-1) or (b > m-1) or (a < 0) or (b < 0):
            continue
        new_dice = [0,0,0,0,0,0]
        new_dice[0] = dice[3]
        new_dice[3] = dice[5]   
        new_dice[2] = dice[0]     
        new_dice[5] = dice[2]   
        new_dice[1] = dice[1]
        new_dice[4] = dice[4]
    if move == 2:
        a,b = x, y-1
        if (a > n-1) or (b > m-1) or (a < 0) or (b < 0):
            continue
        new_dice = [0,0,0,0,0,0]
        new_dice[0] = dice[2]
        new_dice[2] = dice[5]   
        new_dice[3] = dice[0]     
        new_dice[5] = dice[3]   
        new_dice[1] = dice[1]
        new_dice[4] = dice[4]
    if move == 3:
        a,b = x-1, y
        if (a > n-1) or (b > m-1) or (a < 0) or (b < 0):
            continue
        new_dice = [0,0,0,0,0,0]
        new_dice[0] = dice[4]
        new_dice[4] = dice[5]   
        new_dice[5] = dice[1]     
        new_dice[1] = dice[0] 
        new_dice[2] = dice[2]
        new_dice[3] = dice[3]
    if move == 4:
        a,b = x+1, y
        if (a > n-1) or (b > m-1) or (a < 0) or (b < 0):
            continue
        new_dice = [0,0,0,0,0,0]
        new_dice[0] = dice[1]
        new_dice[1] = dice[5]   
        new_dice[5] = dice[4]     
        new_dice[4] = dice[0]  
        new_dice[2] = dice[2]
        new_dice[3] = dice[3]
    if pan[a][b] == 0:
        pan[a][b] = new_dice[5]
    else:
        new_dice[5] = pan[a][b]  
        pan[a][b] = 0
    print(new_dice[0])
    dice = new_dice
    x,y = a,b