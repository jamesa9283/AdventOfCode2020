# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 10:21:01 2020

@author: james
"""

import re

fname = './input.txt'

n = 0
res = 0

with open(fname) as f:
    entries = f.read().split('\n\n')

for ans in entries:
    rep = ans.split('\n')
    #print(rep)
    ans = []
    for i in range(len(rep)):
        for j in range(len(rep[i])):
            ans.append(rep[i][j])
        for lett in set(ans):
            if ans.count(lett) == len(rep):
                res += 1
    
print(res)