#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 09:37:56 2019

@author: donsdev
"""

#1546 평균
    
N = int(input());
input_scores = []
new_scores = []
for score in map(int, input().split()):
    input_scores.append(score)

M = max(input_scores)
for score in map(lambda x : x / M * 100, input_scores):
    new_scores.append(score)

print(sum(new_scores)/N)