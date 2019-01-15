#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 15:54:26 2019

@author: donsdev
"""
def is_prime(n):
    if n <= 1:
        return 0
    i = 2
    while i*i <= n:
        if n % i == 0:
            return 0
        i+=1
    return 1

a,b = map(int, input().split())
for i in range(a,b+1):
    if is_prime(i):
        print(i)