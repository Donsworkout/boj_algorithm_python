#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 21:06:59 2019

@author: donsdev
"""
import time
start_time = time.time()

def quicksort(start,end,arr):
    pivot,j,i = start,start,start + 1
    if start < end :
        while i <= end:
            if arr[i] < arr[pivot]:
                j+=1
                arr[i],arr[j] = arr[j],arr[i]
            i+=1
            
        arr[pivot],arr[j] = arr[j],arr[pivot]
        pivot = j
        
        quicksort(start,pivot-1,arr)
        quicksort(pivot+1,end,arr)    
        
arr = [3,5,7,10,12,4,1,88,77,101]
n = 10
quicksort(0,9,arr)
print(arr)

print("--- %s seconds ---" %(time.time() - start_time))

