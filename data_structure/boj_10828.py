#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 00:23:51 2019

@author: donsdev
"""
#스택
import sys
input = sys.stdin.readline

n = int(input())
stk = []
for _ in range(n):
    s = input().split()
    com = s[0]
    if len(s) != 1:
        var = s[1]
    if com == 'push':
        stk.append(int(var))
    elif com == 'pop':
        if stk:
            print(stk[-1])
            stk.pop()
        else:
            print("-1")
    elif com == 'size':
        print(len(stk))   
    elif com == 'empty':
        if stk:
            print("0")
        else:
            print("1")
    elif com == 'top':
        if not stk:
            print("-1")
        else:
            print(stk[-1])