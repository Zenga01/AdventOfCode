# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 12:22:07 2020

@author: Jelle Idzenga
"""
from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

f=open("input.txt")
instructions=f.read().split('\n')
buses=instructions[1].split(',')
busIDs=[int(s) for s in buses if s.isdigit()]
index=[(ID-(buses.index(str(ID))%ID))%ID for ID in busIDs]
time=chinese_remainder(busIDs,index)