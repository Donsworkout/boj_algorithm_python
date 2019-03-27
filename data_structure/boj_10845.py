#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 12:20:22 2019

@author: donsdev
"""

#import sys
#input = sys.stdin.readline

n = int(input())
stk = []
for _ in range(n):
    s = input().split()
    com = s[0]
    if len(s) != 1:
        var = s[1]
    if com == 'push':
        stk.insert(0,int(var))
    elif com == 'pop':
        if stk:
            print(stk.pop())
        else:
            print('-1')
    elif com == 'size':
        print(len(stk))   
    elif com == 'empty':
        if stk:
            print("0")
        else:
            print("1")
    elif com == 'front':
        if not stk:
            print('-1')
        else:
            print(stk[-1])
    elif com == 'back':
        if not stk:
            print("-1")
        else:
            print(stk[0])