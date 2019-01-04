#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 11:51:25 2019

@author: donsdev
"""

T = int(input())
for i in range(0,T):
    print_str = ""
    R, input_str = input().split()
    for elem in input_str:
        print_str += int(R) * elem
    print(print_str)
