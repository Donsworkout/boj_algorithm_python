#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 19:50:49 2019

@author: donsdev
"""
import collections

def BFS():
    cnt = 0
    while queue:
        q_size = len(queue)
        for _ in range(q_size):
            cur = queue.popleft()
            if cur == k:
                return cnt
            if not visited[cur+1] and (cur+1 <= 100000):
                queue.append(cur+1)
                visited[cur+1] = 1   
            if not visited[cur-1] and (cur-1 >= 0):
                queue.append(cur-1)
                visited[cur-1] = 1   
            if not visited[cur*2] and (cur*2 <= 100000):
                queue.append(cur*2)
                visited[cur*2] = 1         
        cnt += 1
        
visited = [0] * 200002
n,k = map(int,input().split())
queue = collections.deque([n])
visited[n] = 1
print(BFS())