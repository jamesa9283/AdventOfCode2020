# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 10:56:05 2020

@author: james
"""

import numpy as np

fname = './input.txt'
rup = 127
rlw = clw = 0
cup = 7
sID = 0
ids = []

def cbins(inst, up, lw):
    for i in range(len(str(inst))):
        if inst[i] == 'L':
            up = up - np.ceil(0.5 * (up - lw))
        if inst[i] == 'R':
            lw = lw + np.ceil(0.5 * (up - lw))
    return int(up)

def rbins(inst, up, lw):
    for i in range(len(str(inst))):
        if inst[i] == 'F':
            up = up - np.ceil(0.5 * (up - lw))
        if inst[i] == 'B':
            lw = lw + np.ceil(0.5 * (up - lw))
    return int(up)

with open(fname) as f:
    passes = f.read().splitlines()

for code in passes:
    r = rbins(code, rup, rlw)
    c = cbins(code, cup, clw)
    sID = 8 * r + c
    ids.append(sID)
#print(sorted(ids))
    
for i in ids:
    if (i + 1) not in ids:
        print(i + 1)
    
    
    
#print(cbins('FBFBBFFRLR', cup, clw))


