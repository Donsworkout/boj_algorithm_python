#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 20:45:09 2019

@author: donsdev
"""

n,k = map(int,input().split())
coins = []
for i in range(n):
    coins.append(int(input()))
coins.reverse()
cnt = 0
while k != 0:
    for coin in coins:
        if coin <= k:
            cnt += k // coin
            k = k - (coin * (k // coin))            
            break
print(cnt)
            