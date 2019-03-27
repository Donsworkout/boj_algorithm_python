#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 스택 관련 문제
"""
Created on Fri Jan 11 14:04:49 2019

@author: donsdev
"""
n = int(input())
for _ in range(n):
    stack = []
    minus = 0
    p_str = input()
    for elem in p_str:
        if elem == "(":
            stack.insert(0,elem)
        else:
            if stack:
                stack.pop()
            else:
                minus = 1
                break
            
    if stack or (not stack and minus):
         print("NO")       
    else:
        print("YES")