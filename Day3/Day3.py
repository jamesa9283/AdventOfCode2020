# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 10:07:36 2020

@author: james
"""

free = 0
trees = 0
sumt = []
res = 1
fname = "./input.txt"
nums = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
#nums = [[3, 1]]



with open(fname) as f:
    content = f.read().splitlines()
    
#print(content)

for j in nums:
    for i in range(int(len(content)/int(j[1]))):
#        if content[(i * j[1])][int((j[0]*(i)))%int(len(content[0]))] == '.':
#            free = free + 1
        if content[i * j[1]][int((j[0]*(i)))%int(len(content[0]))] == '#':
            trees = trees + 1
    sumt.append(trees)
    trees = 0
    
for k in sumt:
    res = k * res
print(res)
    #
    