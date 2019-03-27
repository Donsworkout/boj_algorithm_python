#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 09:48:47 2019

@author: donsdev
"""
board = [['U','R','L','P','M'],['X','P','R','E','T'],['G','I','A','E','T'],['X','T','N','Z','Y'],['X','O','Q','R','S']]
direction = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
sw = False

def detector(y,x,word):
    if x < 0 or y < 0 or x > 4 or y > 4:
        return False 
    if word[0] != board[y][x]:
        return False
    if len(word) == 1:
        return True
    for tup in direction:
        if detector(y+tup[0], x+tup[1], word[1:]):
            return True
    return False
    
if __name__ == "__main__":
    word = input()
    for i in range(0,5):
        for j in range(0,5):
            if word[0] == board[i][j] and detector(i,j,word) == True:
                sw = True
                break
if sw == True:
    print(True)
else:
    print(False)
                    