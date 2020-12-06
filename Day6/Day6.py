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
            if rep[i][j] not in ans: # you can probably use `set` here
                ans.append(rep[i][j])
    res += len(ans)
    
print(res)