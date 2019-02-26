#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 12:56:36 2019

@author: donsdev
"""
import collections 

def complete():
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if box[i][j][k] == 0:
                    return False
    return True 

def bfs():
    cnt = 0
    while queue:
        q_size = len(queue)
        for _ in range(q_size):
            cur = queue.popleft()
            x,y,z= cur[0],cur[1],cur[2]
            if x+1 < h and box[x+1][y][z] == 0:
                queue.append((x+1,y,z))
                box[x+1][y][z] = 1
            if y+1 < n and box[x][y+1][z] == 0:
                queue.append((x,y+1,z))
                box[x][y+1][z] = 1
            if z+1 < m and box[x][y][z+1] == 0:
                queue.append((x,y,z+1))
                box[x][y][z+1] = 1
            if x-1 >= 0 and box[x-1][y][z] == 0:
                queue.append((x-1,y,z))
                box[x-1][y][z] = 1
            if y-1 >= 0 and box[x][y-1][z] == 0:
                queue.append((x,y-1,z))
                box[x][y-1][z] = 1
            if z-1 >= 0 and box[x][y][z-1] == 0:
                queue.append((x,y,z-1))
                box[x][y][z-1] = 1
        if not queue and complete():
            return cnt 
        elif not queue and not complete():
            return -1
        cnt += 1
        
m,n,h = map(int,input().split())
box = [[[0]*m for i in range(n)] for j in range(h)]
queue = collections.deque([])

for i in range(h):
    for j in range(n):
        spd = list(map(int,input().split()))
        for k in range(m):
            box[i][j][k] = spd[k]
            if spd[k] == 1:
                queue.append((i,j,k))
if complete():
    print(0)
else:
    print(bfs())