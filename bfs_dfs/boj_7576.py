#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 14:12:25 2019

@author: donsdev
"""
import collections

def all_riped():
    global m,n
    for i in range(n):
        for j in range(m):
            if adj[i][j] == 0:
                return False
    return True

def BFS():
    cnt = 0
    global queue,adj
    while queue:
        q_size = len(queue)
        for _ in range(q_size):
            cur = queue.popleft()
            x,y = cur[0],cur[1]
            if x+1 < n and adj[x+1][y] == 0:
                queue.append((x+1,y))
                adj[x+1][y] = 1
            if y+1 < m and adj[x][y+1] == 0:
                queue.append((x,y+1))
                adj[x][y+1] = 1
            if x-1 >= 0 and adj[x-1][y] == 0:
                queue.append((x-1,y))
                adj[x-1][y] = 1
            if y-1 >= 0 and adj[x][y-1] == 0:
                queue.append((x,y-1))
                adj[x][y-1] = 1  
                
            if len(queue) == 0 and all_riped():
                return cnt
            elif len(queue) == 0 and not all_riped():
                return -1
        cnt += 1
    
m,n = map(int,input().split())
adj = []
queue = collections.deque([]);
for i in range(0,n):
    adj.append(list(map(int,input().split())))
    for j in range(0,m):
        if adj[i][j] == 1:
            queue.append((i,j))
print(BFS())