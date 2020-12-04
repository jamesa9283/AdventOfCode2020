# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 08:53:47 2020

@author: james
"""
import re

n =0

data = ['eyr:2028 ecl:gry hgt:171cm byr:1960 iyr:2020\npid:688526729 cid:262\nhcl:#733820\n']
vtrs = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

clrs = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

for point in data:
    for vtr in vtrs:
        if vtr in point: 
            #print(point)
            i = point.index(vtr)
            #print(i)
            if vtrs.index(vtr) == 0:
                if int(point[i+4:i+8]) >= 1920 and int(point[i+4:i+8]) <= 2002:
                    n = n + 1
            if vtrs.index(vtr) == 1:
                if int(point[i+4:i+8]) >= 2010 and int(point[i+4:i+8]) <= 2020:
                    n = n + 1
            if vtrs.index(vtr) == 2:
                if int(point[i+4:i+8]) >= 2020 and int(point[i+4:i+8]) <= 2030:
                    n = n + 1
            if vtrs.index(vtr) == 3:
                if 'cm' in point:
                    if int(point[i+4:i+7]) >= 150 and int(point[i+4:i+7]) <= 193:
                        n = n + 1
                if 'in' in point:
                    if int(point[i+4:i+6]) >= 59 and int(point[i+4:i+6]) <= 76:
                        n = n + 1
            if vtrs.index(vtr) == 4:
                if re.fullmatch("^[#a-f0-9]*$", point[i+4:i+11]):
                    n = n + 1
            if vtrs.index(vtr) == 5:
                if point[i+4:i+7] in clrs:
                    n = n + 1
            if vtrs.index(vtr) == 6:
                if re.fullmatch("^[0-9]*$", point[i+4:i+11]):
                    n = n + 1 
        else:
            print('no')

print(n)
    

    