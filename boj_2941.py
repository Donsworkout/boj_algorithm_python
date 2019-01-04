#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 13:38:06 2019

@author: donsdev
"""

#단어 조각별로 리스트 놓고 그거 iter 돌면서 일치하는거 있을 때마다 삭제 + 갯수 세기
targets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
input_str = input()
for elem in targets:
    input_str = input_str.replace(elem,'0')
print(len(input_str))