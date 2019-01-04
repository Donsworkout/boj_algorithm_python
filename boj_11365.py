#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 12:18:19 2019

@author: donsdev
"""

while True:
    para = input()
    if para == "END":
        break
    print(para[::-1])