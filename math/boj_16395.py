ㅊ#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 13:08:49 2019

@author: donsdev
"""
d = [[-1]*31 for _ in range(31)]

def pascal(n,r):
    if r == 0 or r == n:
        return 1
    if d[n][r] != -1:
        return d[n][r]
    else:
        d[n][r] = pascal(n-1,r-1) + pascal(n-1,r)
        return d[n][r]
        
n,k = map(int,input().split())
print(pascal(n-1,k-1))