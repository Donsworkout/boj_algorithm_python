#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 13:28:58 2019

@author: donsdev
"""

pieces = input().split("-")
made_str = ""
for piece in pieces:
    made_str += piece[0]
print(made_str)
