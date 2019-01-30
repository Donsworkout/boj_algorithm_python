#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 18:03:28 2019

@author: donsdev
"""
"""
    if i == 0:
       d[0][0], d[0][1], d[0][2] = a,b,c
"""         
    
n = int(input())
d = [[0,0,0]]
p = [[0,0,0]]
d[0] = [0,0,0]
for _ in range(n):
    a,b,c = map(int,input().split())
    p.append([a,b,c])
i=1
while i < n+1:   
    d.append([min(d[i-1][1],d[i-1][2]) + p[i][0], min(d[i-1][0],d[i-1][2]) + p[i][1] , min(d[i-1][0],d[i-1][1]) + p[i][2]])
    i+=1
print(min(d[n]))