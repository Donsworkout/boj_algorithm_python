#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 13:08:52 2019

@author: donsdev
"""

def muhan(n):
    global P,Q,A
    if A.get(n):
        return A[n]
    else:
        A[n] = muhan(int(n/P)) + muhan(int(n/Q))
        return A[n]
n,P,Q = map(int,input().split())
A= {}
A[0] = 1
print(muhan(n))