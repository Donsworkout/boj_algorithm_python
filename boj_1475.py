#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 16:44:00 2019

@author: donsdev
"""
lst_group = [[] for rows in range(7)]
cache = []

def toggle(elem):
    if elem == '6':
        return '9'
    else:
        return '6'
    
def divider(n):
    global lst_group
    for elem in n:
        if elem == '6' or elem == '9':
            for lst in lst_group:
                if elem in lst:
                    if toggle(elem) in lst:
                        next
                    else:
                        lst.append(toggle(elem))
                        break
                else: 
                    lst.append(elem)
                    break       
        else:       
            for lst in lst_group:
                if elem in lst:
                    next
                else: 
                    lst.append(elem)
                    break
cnt = 0
n = input()
divider(n)
for lst in lst_group:
    if lst != []:
        cnt += 1
print(cnt)
        

    