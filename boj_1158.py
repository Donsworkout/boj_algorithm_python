#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 16:42:06 2019

@author: donsdev
"""
#import sys
#input = sys.stdin.readline

class Queue():
    def __init__(self,size):
        self.max_size = size
        self.size = 0
        self.front = -1
        self.rear = -1
        self.arr = [-1] * size
        
    def enqueue(self,data):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.max_size
            self.arr[self.rear] = data
            self.size += 1
            
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.max_size
            self.size -= 1
            return self.arr[self.front]
        
    def isFull(self):
        return self.size == self.max_size
    
    def isEmpty(self):
        return self.size == 0
    
n,m = map(int,input().split())
queue = Queue(n)

for i in range(1,n+1):
    queue.enqueue(str(i))

string = ''
while not queue.isEmpty():
    for _ in range(m-1):
        queue.enqueue(queue.dequeue())
    if queue.size == 1:
        string += str(queue.dequeue()) + '>'
    else:
        string += str(queue.dequeue()) + ', '  
print('<',end='')
print(string)
