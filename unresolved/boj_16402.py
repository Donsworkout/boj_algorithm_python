#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 14:27:44 2019

@author: donsdev
"""

a,b = map(int,input().split())
has_many = {}
belongs_to = {}

for i in range(a):
    t = input()
    belongs_to[t] = None
    has_many[t] = []
for _ in range(b): 
    x,y,z = input().split(',')
    if z == '1':
        belongs_to[y] = x
        has_many[x].append(y)
        belongs_to[x] = None  
        has_many[y] = []
        for elem in has_many[y]:
            if elem != x: 
                belongs_to[elem] = x
                has_many[x].append(elem)
    elif z == '2':
        belongs_to[x] = y
        has_many[y].append(x)
        belongs_to[y] = None  
        has_many[x] = []
        for elem in has_many[x]:
            if elem != y:
                belongs_to[elem] = y
                has_many[y].append(elem)   
print(has_many)
print(belongs_to)
"""
Kingdom of A
Kingdom of B
Kingdom of C
Kingdom of D
Kingdom of E
Kingdom of A,Kingdom of B,2
Kingdom of C,Kingdom of D,1
Kingdom of E,Kingdom of C,2
Kingdom of A,Kingdom of C,1
"""

