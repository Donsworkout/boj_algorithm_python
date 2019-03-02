#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 14:23:44 2019

@author: donsdev
"""
import collections 
dir_1 = [(1,0),(0,1),(-1,0),(0,-1)]

def possible(a,b):
    if a < n and a >= 0 and b < m and b >= 0:
        return True
    else:
        return False
        
def BFS():
    cnt = 0
    while queue:
        len_q = len(queue)
        for _ in range(len_q):
            cur = queue.popleft()
            x,y,chance = cur[0],cur[1],cur[2]
            if (x == n-1) and (y ==  m-1):
                return cnt
            for elem in dir_1:
                a,b = x + elem[0], y + elem[1]
                if chance:
                    if possible(a,b) and not visited_2[a][b]:
                        if wall[a][b] == '0':
                                queue.append((a,b,chance))
                                visited[a][b] = 1
                        else:
                            if chance:
                                queue.append((a,b,False))
                                visited_2[a][b] = 1                      
                else:                   
                    if possible(a,b) and not visited[a][b]:
                        if wall[a][b] == '0':
                                queue.append((a,b,chance))
                                visited[a][b] = 1
                        else:
                            if chance:
                                queue.append((a,b,False))
                                visited_2[a][b] = 1  
        cnt += 1
    return -2
        
n,m = map(int,input().split())
cnt = 0
wall = []
visited = [[0] * 1001 for rows in range(1001)]
queue = collections.deque([(0,0,True)])
visited[0][0] = 1
visited_2 = [[0] * 1001 for rows in range(1001)]
for _ in range(n):
    wall.append(input())
print(BFS()+1)