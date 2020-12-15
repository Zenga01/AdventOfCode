# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 10:26:58 2020

@author: Jelle Idzenga
"""
# from toolz import memoize, concatv, frequencies, drop

import time

f=open("Advend10.txt")
adap=[int(a) for a in f.read().split('\n')]
adapters=[0]+adap+[max(adap)+3]
adapters.sort()
currentJoltage=0;
diff1=0;
diff3=0;
for joltage in adapters:
    if joltage==currentJoltage+1:
        currentJoltage=joltage
        diff1+=1;
    elif joltage==currentJoltage+3:
        diff3+=1;
        currentJoltage=joltage
print(diff1*(diff3+1))
starttime=time.perf_counter()
n=len(adapters)
paths=[0]*n
paths[0]=1;
for i in range(n):
    for j in range(1,4):
        if (i+j)>=n:
            continue
        difference=adapters[i+j]-adapters[i]
        if difference<=3:
            paths[i+j]+=paths[i]
timeTaken=time.perf_counter()-starttime