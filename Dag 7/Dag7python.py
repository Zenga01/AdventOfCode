# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 08:45:14 2020

@author: Jelle Idzenga
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import re

def findBags(ruleDictionary,bagColor):
    possibleBags=[];
    for ruleKey in ruleDictionary:
        for bag in ruleDictionary[ruleKey]:
            if bagColor in bag:
                possibleBags.append(ruleKey);
                possibleBags+=findBags(ruleDictionary,ruleKey)
    return possibleBags            

def countInsideBags(ruleDictionary,bagColor):
    count=0;
    if bagColor in ruleDictionary:
        for inBag in ruleDictionary[bagColor]:
            if (inBag=='no other'):
                continue
            inBags=inBag.split(' ',1)
            count+=int(inBags[0])+int(inBags[0])*countInsideBags(ruleDictionary,inBags[1])
    return count



f=open("Rules.txt")
rules=f.read().split("\n")
ruleDict={}
for i in rules:
    ruleSplit=i.split(' bags contain ');
    bag=ruleSplit[0];
    ruleSplit[1].strip('bags.')
    containing=re.split(' bags, | bag, ',ruleSplit[1])
    containing=[i.replace(' bags.','').replace(' bag.','') for i in containing]
    ruleDict[bag]=containing;
    
    
possibleBags=findBags(ruleDict,'shiny gold')
print(len(set(findBags(ruleDict,'shiny gold'))))
print(countInsideBags(ruleDict, 'shiny gold'))



    
        