#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 17:38:55 2019

@author: donsdev
"""

def DFS(x,y):
    global cnt
    visited[x][y] = 1
    cnt += 1
    if x+1 < n and not visited[x+1][y] and graph[x+1][y] == '1':
        DFS(x+1,y)
    if y+1 < n and not visited[x][y+1] and graph[x][y+1] == '1':
        DFS(x,y+1)
    if x-1 >= 0 and not visited[x-1][y] and graph[x-1][y] == '1':
        DFS(x-1,y)
    if y-1 >= 0 and not visited[x][y-1] and graph[x][y-1] == '1':
        DFS(x,y-1)
    return cnt

n = int(input())
visited = [[0]*n for row in range(n)]
graph = [[0]*n for row in range(n)]
arr = []
for i in range(n):
    graph[i] = input()
    for j in range(n):
        if graph[i][j] =='1':
            arr.append((int(i),int(j)))
entry = []
total = 0
for e in arr:
    if not visited[e[0]][e[1]]:
        cnt = 0
        total += 1
        entry.append(DFS(e[0],e[1]))
print(total)
for elem in sorted(entry):
    print(elem)