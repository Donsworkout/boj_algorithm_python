#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 18:22:31 2019

@author: donsdev
"""
import collections
moves = [(1,0),(-1,0),(0,1),(0,-1)]
def bfs():
    cnt = 0
    while q_red:
        if cnt >= 10:
            return -1
        len_q = len(q_red)
        for _ in range(len_q):
            cur_red = q_red.popleft()
            cur_blue = q_blue.popleft()
            rx,ry = cur_red[0],cur_red[1]
            bx,by = cur_blue[0],cur_blue[1]  
            if pan[rx][ry] == 'O' and pan[rx][ry] != pan[bx][by]:
                return cnt
            for move in moves:
                m_rx,m_ry,m_bx,m_by = rx,ry,bx,by
                while pan[m_rx + move[0]][m_ry + move[1]] != '#' and pan[m_rx][m_ry] != 'O':
                    m_rx += move[0]
                    m_ry += move[1]   
                while pan[m_bx + move[0]][m_by + move[1]] != '#' and pan[m_bx][m_by] != 'O':
                    m_bx += move[0]
                    m_by += move[1]  
                if (m_rx == m_bx) and (m_ry == m_by):
                    if pan[m_rx][m_ry] == 'O':
                        continue
                    if abs(m_rx - rx) + abs(m_ry - ry) < abs(m_bx - bx) + abs(m_by - by):
                        m_bx -= move[0]
                        m_by -= move[1]
                    else:
                        m_rx -= move[0]
                        m_ry -= move[1]
                if visited_red[m_rx][m_ry] and visited_blue[m_bx][m_by]:
                    continue
                q_red.append((m_rx,m_ry))
                visited_red[m_rx][m_ry] = 1
                q_blue.append((m_bx,m_by))
                visited_blue[m_bx][m_by] = 1 
        cnt += 1
    return -1
                    
                    
n,m = map(int,input().split())
pan = []
q_red = collections.deque([])
q_blue = collections.deque([])
visited_red = [[0] * m for rows in range(n)]
visited_blue = [[0] * m for rows in range(n)]
for i in range(n):
    pan.append(input())
    for j in range(m):
        if pan[i][j] == 'R':
            q_red.append((i,j))
            visited_red[i][j] = 1
        elif pan[i][j] == 'B':
            q_blue.append((i,j))
            visited_blue[i][j] = 1       
print(bfs())

