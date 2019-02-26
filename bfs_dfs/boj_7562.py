#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 23:02:50 2019

@author: donsdev
"""
import collections 
move = [(-1,2),(-2,1),(-2,-1),(-1,-2),(1,2),(2,1),(2,-1),(1,-2)]

def possible_range(a,b):
    if a < 0 or b < 0 or a >= l or b >= l:
        return False
    else:
        return True
        
def BFS():
    cnt = 0
    while queue:
        len_q = len(queue)
        for _ in range(len_q):
            cur = queue.popleft()
            if cur == target:
                return cnt
            x,y = cur[0],cur[1]
            for e in move:
                if possible_range(x+e[0],y+e[1]) and not visited[x+e[0]][y+e[1]]:
                    queue.append((x+e[0],y+e[1]))
                    visited[x+e[0]][y+e[1]] = 1
        cnt += 1
            
for _ in range(int(input())):
    l = int(input())
    visited = [[0]*l for row in range(l)]
    queue = collections.deque([])
    c = tuple(map(int,input().split()))
    queue.append(c)
    visited[c[0]][c[1]] = 1
    target = tuple(map(int,input().split()))
    print(BFS())