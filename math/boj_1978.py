#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 08:57:58 2019

@author: donsdev
"""
n = int(input())
nstr = list(map(int,input().split()))
cnt = 0

def is_prime(n):
    if n < 2:
        return 0
    i = 2
    while i * i <= n:
        if n % i == 0:
            return 0
        i+=1
    return 1
        
for elem in nstr:
    if is_prime(elem):
        cnt += 1

print(cnt)