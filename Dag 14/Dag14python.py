# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 11:46:49 2020

@author: Jelle Idzenga
"""
import re

def applyMask(elem, mask):
    elem=int(elem)
    elem|=int(mask.replace('X','0'),2)
    elem&=int(mask.replace('X','1'),2)
    return elem

f=open("input.txt")
instructions=f.read().split('\n')
instructions=[i.split(' = ') for i in instructions]
print(applyMask(instructions[1][1], instructions[0][1]))

 

print(applyMask(0, 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'))
mem={}
for instruction in instructions:
    if instruction[0]=='mask':
        mask=instruction[1];
    else:
        address=instruction[0][4:-1]
        mem[address]=applyMask(instruction[1], mask)
total=0
for elem in mem:
    total+=mem[elem];
print(total)