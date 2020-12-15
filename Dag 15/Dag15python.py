# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 10:24:41 2020

@author: Jelle Idzenga
"""
import time

end=30000000
start=[0,8,15,2,12,1,4]
start=[2,3,1    ]
lastTime={}
for nr in range(len(start)):
    lastTime[start[nr]]=nr
i=len(start)
curr=start[i-1]
starttime=time.perf_counter()
while i<end:
    prev=curr
    if prev in lastTime:
        curr=(i-1-lastTime[prev])
    else:
        curr=0
    lastTime[prev]=i-1
    i+=1
print(curr)
timeTaken=time.perf_counter()-starttime