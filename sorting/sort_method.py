#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 21:18:43 2019

@author: donsdev
"""
import time
start_time = time.time()

arr = [3,5,7,10,12,4,1,88,77,101]
arr.sort(key=int, reverse=True)
print(arr)

print("--- %s seconds ---" %(time.time() - start_time))