#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 14:44:27 2019

@author: donsdev
"""
x,y,w,h = map(int,input().split())
print(min(x,y,w-x,h-y))