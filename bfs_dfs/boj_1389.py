#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 00:40:40 2019

@author: donsdev
"""
import collections 

def BFS(queue,target):
    cnt = 0
    while queue:
        len_q = len(queue)
        for _ in range(len_q):
            cur = queue.popleft()
            if cur == target:
                return cnt
            for elem in friend[cur]:
                if not visited[elem]:
                    queue.append(elem)
                    visited[elem] = 1
        cnt += 1
    return 0
n,m = map(int,input().split())
friend = {}
arr = []
for _ in range(m):
    s,o = map(int,input().split())
    if s in friend:
        friend[s].append(o)  
    else:
        friend[s] = [o]
    if o in friend:
        friend[o].append(s)  
    else:
        friend[o] = [s]
for i in range(1,n+1):
    total = 0
    for j in range(1,m+1):
        if j != i:
            visited = [0] * (n + 1)
            total += BFS(collections.deque([i]),j)
    arr.append(total)
print(arr.index(min(arr))+1)
