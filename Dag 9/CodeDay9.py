# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 23:38:12 2020

@author: Jelle Idzenga
"""
f=open("input.txt")
inputtxt=[int(a) for a in f.read().split('\n')]
found=False;
for i in range(25,len(inputtxt)-1):
    found=False;
    sumValues=inputtxt[i-25:i];
    for j in range(1,25):
        if (inputtxt[i] in [x+sumValues[j] for x in sumValues]):
            found=True;
    if found!=True:
        p1=inputtxt[i]
        break

setFound=False;

for i in range(len(inputtxt)):
    for j in range(i+1,len(inputtxt)):
        if ( i+1 != j) and sum(inputtxt[i:j])==p1:
            p2=min(inputtxt[i:j])+max(inputtxt[i:j]);
            break;
print(p1)
print(p2)    