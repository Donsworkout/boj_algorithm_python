#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 09:51:36 2019

@author: donsdev
실패함
"""

n = int(input())
for _ in range(n):
    s,e = map(int,input().split())
    dist = e - s
    pos,cnt,i = 1,1,2
    while pos < dist:
        pos += i / 2
        cnt += 1
        i += 1
        print(pos,dist,i,cnt)
    print(cnt)