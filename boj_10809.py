#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 11:02:15 2019

@author: donsdev
"""
#boj 10809 알파벳
# * 리스트 앞에 쓰면 그냥 다 스트립해서 뽑아줌
atoz = []
for i in range(0,26):
    atoz.append(-1)
target = input()
for idx, l in enumerate(target):
    target_idx = ord(l) - 97
    if atoz[target_idx] == -1 :
        atoz[target_idx] = idx
print(*atoz)