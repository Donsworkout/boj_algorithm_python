#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 17:30:59 2019

@author: donsdev
"""

graph = {1: [2, 3], 2: [4, 5],
                    3: [5], 4: [6], 5: [6],
                    6: [7], 7: []}

def dfs_recursive(graph, root, path=[]):
    path+=[root] ###root 방문.

    for node in graph[root]:  ##root 노드에 연결된 node 수 만큼 반복
        if node not in path: ##아직 방문하지 않은 경우에만
           dfs_recursive(graph, node, path) ##재귀 호출
    
    return path

print(dfs_recursive(graph, 1))


