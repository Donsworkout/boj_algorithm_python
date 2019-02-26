#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 21:05:57 2019

@author: donsdev
"""
def DFS(e):
    global total
    visited[e[0]][e[1]] = 1
    if e in range_dict:
        r = range_dict[e]
        x,y = e[0],e[1]
        for k in range(1,r+1):
            if x + k <= 5000:
                if visited[x+k][y] != 1:
                    DFS((x+k,y))
                else:
                    return True
            if y + k <= 5000:
                if visited[x][y+k] != 1:
                    DFS((x,y+k))  
                else:
                    return True
            if x - k >= 0:
                if visited[x-k][y] != 1:
                    DFS((x-k,y)) 
                else:
                    return True
            if y - k >= 0:
                if visited[x][y-k] != 1:
                    DFS((x,y-k)) 
                else:
                    return True
        total += 1
    return True 

for _ in range(int(input())):
    n = int(input())
    base=[]
    visited=[[0]*5001 for row in range(5001)]
    range_dict = {}
    for _ in range(n):
        x,y,r = map(int,input().split())
        base.append((x,y))
        range_dict[(x,y)] = r
    total = 0
    for e in base:
        if visited[e[0]][e[1]] != 1:
            DFS(e)
    print(total)