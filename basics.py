#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 15:35:01 2021

@author: keitilo
"""
weights = [6.4, 8.2, 8.8, 9.2, 7.2]

 
avg_weight = sum(weights)/len(weights)
   
print(avg_weight)

def average(x):
    if len(x) == 0:
        raise ValueError('input list x is empty')
    else:
        return sum(x)/len(x)

print(average(weights))
empty = []
print(average(empty))


import math

def median(x):
    x.sort()
    if len(x)%2 == 0:
        return x[len(x)/2] + x[len(x)/2 - 1]
    else:
        return math.ceil(x[len(x)/2])
    
a = [ 1, 3, 2, 4]

print(median(a))