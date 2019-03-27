#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 01:30:25 2019

@author: donsdev
"""
import sys
input = sys.stdin.readline

소수니 = [0] * 10001

def is_prime(n):
    if n < 2:
        return 0
    i = 2
    while i * i <= n:
        if n % i == 0:
            return 0
        i+=1
    return 1

for i in range(2,10001):
    if is_prime(i):
        소수니[i] = 1
        
n = int(input())
for _ in range(n):
    target = int(input())
    i = 2
    min_i = target
    while i < target - 1:
        if 소수니[i] and 소수니[target - i]:
            if abs(2*i - target) < abs(2*min_i - target):
                min_i = i
        i += 1
    print(str(min_i) + " " + str(target - min_i))  