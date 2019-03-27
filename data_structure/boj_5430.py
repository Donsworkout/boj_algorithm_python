#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 15:10:35 2019

@author: donsdev
"""
#DEQUE 관련 문제
#import sys
#input = sys.stdin.readline
n = int(input())
for _ in range(n):
    front = 0
    btn = 1
    cmd = str(input())
    m = int(input())
    s = input().replace('[', '').replace(']', '')
    if m != 0:
        lst = list(map(int,s.split(',')))
    else:
        lst = []
    for elem in cmd:
        if elem == 'R':
            if front == 0:
                front = len(lst) - 1
            else:
                front = 0              
        elif elem == 'D':
            if len(lst) != 0:
                if front == 0:
                    lst.pop(0)
                else:
                    lst.pop()                 
            else:
                print('error')
                btn = 0
                break
    if btn:
        if front == 0:
            print('[',end='')
            print(*lst,sep=',',end='')
            print(']')
        else:
            print('[',end='')
            print(*lst[::-1],sep=',',end='')
            print(']')