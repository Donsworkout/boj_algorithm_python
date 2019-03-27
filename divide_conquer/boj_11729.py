#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 16:16:07 2019

@author: donsdev
"""
path_list = []

def move(begin, end):
    path_list.append(begin + " " + end)
    
def hanoi_move(n,begin,med,end):
    if n == 1:
        move(begin,end)
    else:
        hanoi_move(n-1,begin,end,med)
        hanoi_move(1,begin,med,end)
        hanoi_move(n-1,med,begin,end)

n = int(input())
hanoi_move(n,'1','2','3')
print(len(path_list))
print(*path_list, sep ="\n")