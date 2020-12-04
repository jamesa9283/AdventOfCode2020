# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 08:34:00 2020

@author: james


THIS CODE NEEDS TO BE FIXED
"""

import re

n = 0
m = 0
fname = './input.txt'
vtrs = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

clrs = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

with open(fname) as f:
    lines = f.read()

passports = lines.split('\n')

#print(passports)

for point in passports:
    if point == '' or (passports.index(point) == len(passports)):
        if n == 7:
            m = m + 1
        n = 0
    else:
        for vtr in vtrs:
            if vtr in point:
                #print(point)
                i = point.index(vtr)
                #print(i)
                if vtrs.index(vtr) == 0:
                    #print('oi')
                    if 1920 <= int(point[i+4:i+8]) <= 2002:
                        n = n + 1
                if vtrs.index(vtr) == 1:
                    if 2010 <= int(point[i+4:i+8]) <= 2020:
                        n = n + 1
                if vtrs.index(vtr) == 2:
                    if 2020 <= int(point[i+4:i+8]) <= 2030:
                        n = n + 1
                if vtrs.index(vtr) == 3:
                    if ('cm' in point) or ('in' in point):
                            if re.match("[0-9]*$", point[i+4:i+7]) and (150 <= int(point[i+4:i+7]) or 59 <= int(point[i+4:i+6]) <= 76) <= 193:
                                n = n + 1
                if vtrs.index(vtr) == 4:
                    if re.fullmatch("#[0-9a-f]*$", point[i+4:i+11]):
                        n = n + 1
                if vtrs.index(vtr) == 5:
                    if point[i+4:i+7] in clrs:
                        #print(point[i+4:i+7])
                        n = n + 1
                if vtrs.index(vtr) == 6:
                    if re.fullmatch("[0-9]*$", point[i+4:i+11]):
                        n = n + 1
    
    
# add one to this total if not correct
print(m)


# 129 is too high