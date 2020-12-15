# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 12:39:00 2020

@author: Jelle Idzenga
"""
from copy import deepcopy
def checkOccupied(seats,x,y):
    occupied=0
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            r=x+dx
            if dx==0 and dy==0:
                continue
            if not(0<=(x+dx)<len(seats)):
                continue
            if not(0<=(y+dy)<len(seats[x])):
                continue
            if seats[x+dx][y+dy]=='#':
                occupied+=1
    return occupied
def checkOccupied2(seats,x,y):
    occupied=0
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            if dx==0 and dy==0:
                continue
            r=x+dx
            c=y+dy
            if (not(0<=r<len(seats)) or not(0<=c<len(seats[r]))):
                continue
            while seats[r][c]=='.':
                r=r+dx
                c=c+dy
                if (not(0<=r<len(seats)) or not(0<=c<len(seats[r]))):
                    r=r-dx
                    c=c-dy
                    break
            if seats[r][c]=='#':
                occupied+=1
    return occupied        

f=open("input.txt")
rows=[a for a in f.read().split('\n')]
seats=[list(a) for a in rows]
Changed=True;

while Changed==True:
    newseats=deepcopy(seats)
    Changed=False;
    for x in range(len(seats)):
        for y in range(len(seats[x])):
            if(seats[x][y]=='.'):
                continue
            elif(seats[x][y]=='L'):
                numOcc=checkOccupied2(seats,x,y)
                if numOcc==0:
                    newseats[x][y]='#'
                    Changed=True
            elif(seats[x][y]=='#'):
                numOcc=checkOccupied2(seats,x,y)
                if numOcc>=5:
                    newseats[x][y]='L'
                    Changed=True
    seats=deepcopy(newseats)

seatCount=0;
occupiedSeats=[seat=='#' for row in seats for seat in row ]
seatCount=sum([seat=='#' for row in seats for seat in row ])
