# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 10:02:46 2020

@author: Jelle Idzenga
"""

import math
from math import gcd
def lcm(a):
    lcm = a[0]
    for i in a[1:]:
        lcm = lcm*i//gcd(lcm, i)
    return(lcm)

f=open("input.txt")
instructions=f.read().split('\n')
busIDs=[int(s) for s in instructions[1].split(',') if s.isdigit()]
departTime=int(instructions[0])
leaveTimes=[math.ceil(departTime/ID)*ID for ID in busIDs]
waitTime=min([time-departTime for time in leaveTimes])
BusID=busIDs[leaveTimes.index(departTime+waitTime)]
p1=waitTime*BusID
print(p1)

delay=enumerate(instructions[1].split(','))
found=False
timeIncrease=max([int(s) for s in instructions[1].split(',') if s.isdigit()])
time=timeIncrease-int(instructions[1].split(',').index(str(timeIncrease)))
time=0
delay=[[c,e] for c,e in enumerate(instructions[1].split(',')) if e!='x']
print(lcm(busIDs))
timeIncrease=lcm(busIDs)
print(time)
while found==False:
    
    found=True
    time+=timeIncrease
    for count,element in delay:
        if (int((time+count))%int(element))!=0:
            # print("Wrong")
            found=False
            break