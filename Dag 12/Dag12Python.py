# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 13:23:47 2020

@author: Jelle Idzenga
"""
from operator import add
import re
f=open("input.txt")
instructions=f.read().split('\n')
instructions=[list(filter(None,(re.split(r'(\d+)', s)))) for s in instructions]

def rotate(pos,direction,degrees):
    for turn in range(int(degrees/90)):
        if direction==1:
            pos=[pos[1],-pos[0]]
        else:
            pos=[-pos[1],pos[0]]
    return pos
DIRS={'N':[0,1] ,'E':[1,0],'S':[0,-1],'W':[-1,0]}
Turns={'R':1,'L':-1}
DirNrs=['N','E','S',"W"]
startPos=[0,0]
wayPoint=[10,1];
for instruction in instructions:
    instruction[1]=int(instruction[1])
    if instruction[0] in DIRS:
        move=[x*instruction[1] for x in DIRS[instruction[0]]]
        wayPoint=list( map(add, wayPoint, move) )
    else:
        if instruction[0]=='F':
            move=[x*instruction[1] for x in wayPoint]
            startPos=list( map(add, startPos,move ) )
        else:
            wayPoint=rotate(wayPoint,Turns[instruction[0]],instruction[1])
print(sum([abs(x) for x in startPos]))