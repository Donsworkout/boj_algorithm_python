#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 00:47:13 2019

@author: donsdev
"""

def graph_maker(a,b):
    if a not in graph:
        graph[a] = [b]
    else:
        graph[a].append(b)
        
def DFS(cur):
    if cur not in visited:
        visited.append(cur)
        if cur in graph:
            graph[cur].sort()
            for child in graph[cur]:
                DFS(child)

def BFS():
    visited = []
    global queue
    while queue:
        cur = queue.pop(0)
        visited.append(cur)
        graph[cur].sort()
        for child in graph[cur]:
            if child not in visited and child not in queue:
                queue.append(child)
    print(*visited, sep=' ')
    
n,m,v = map(int,input().split())
graph = {}
visited = []
for _ in range(m):
    a,b = map(int,input().split())
    graph_maker(a,b)
    graph_maker(b,a)
DFS(v)
print(*visited, sep=' ')
queue = [v]
BFS()  
    