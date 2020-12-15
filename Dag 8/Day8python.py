# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 06:17:12 2020

@author: Jelle Idzenga
"""

f=open("input.txt")
inputtxt=f.read().split('\n')
instructions=[i.split(' ') for i in inputtxt]


def testInstructions(instructions):
    i=0
    index=[]
    accumulator=0;
    normalTermination=False
    while i not in index:
        if i>=len(instructions):
            print("It works")
            normalTermination=True
            return(True,accumulator)
        index.append(i)
        if instructions[i][0]=='acc':
            accumulator+=int(instructions[i][1])
            i+=1
        elif instructions[i][0]=='nop':
            i+=1
        elif instructions[i][0]=='jmp':
            i+=int(instructions[i][1])
    return (normalTermination,accumulator)
i=0;
index=[]

while i not in index:
        if i>len(instructions):
            normalTermination=True
            break
        index.append(i)
        if instructions[i][0]=='acc':
            i+=1
        elif instructions[i][0]=='nop':
            i+=1
        elif instructions[i][0]=='jmp':
            i+=int(instructions[i][1])  
loop=index
for i in loop:
    if(instructions[i][0]=='jmp'):
        # print("Testing "+str(i))
        instructions[i][0]='nop'
        testCase=testInstructions(instructions)
        instructions[i][0]='jmp'
        # print(testCase)
        if(testCase[0]==True):
            break
    elif(instructions[i][0]=='nop'):
        # print("Testing "+str(i))
        instructions[i][0]='jmp'
        testCase=testInstructions(instructions)
        instructions[i][0]='nop'
        # print(testCase)
        if(testCase[0]==True):
            break