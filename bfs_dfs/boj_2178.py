#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 14:01:12 2019

@author: donsdev
"""
import collections
a = []
visited = [[0] * 100 for _ in range(100)]
moves = [(1,0),(0,1),(-1,0),(0,-1)]

def properRange(x,y):
    if x >= 0 and y >= 0 and x < n and y < m:
        return True
    
def BFS():
    global visited,a,n,m
    cnt = 1
    while len(queue) != 0:
        q_size = len(queue)
        for _ in range(q_size):
            cur = queue.popleft()
            x,y = cur[0],cur[1]
            if (x + 1 == n) and (y + 1 == m):
                return cnt
            for move in moves:
                moved_x, moved_y = x + move[0], y + move[1]
                if properRange(moved_x, moved_y) and a[moved_x][moved_y] == '1' and not visited[moved_x][moved_y]:
                    queue.append((moved_x, moved_y))
                    visited[moved_x][moved_y] = 1
        cnt += 1  
        
n,m = map(int,input().split())
visited[0][0] = 1
for _ in range(n):
    a.append(input())

queue = collections.deque([])
queue.append((0,0))
print(BFS())