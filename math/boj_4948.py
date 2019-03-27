#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 01:00:27 2019

@author: donsdev
"""
#import sys
#input = sys.stdin.readline

소수니 = [0] * 246913

def is_prime(n):
    if n < 2:
        return 0
    i = 2
    while i * i <= n:
        if n % i == 0:
            return 0
        i+=1
    return 1

for i in range(2,246913):
    if is_prime(i):
        소수니[i] = 1
        
while True:
    n = int(input())
    if n == 0:
        break
    else:
        cnt = 0
        for i in range(n + 1, 2*n + 1):
            if 소수니[i]:
                cnt += 1
        print(cnt)