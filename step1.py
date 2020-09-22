# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 12:41:37 2020

@author: yubin
"""
names = ["송중기","송혜교","이종석"]
men = [1,0,1]
heights = [184.3,161.2,186.1]

sum = 0
count = 0
for height in heights:
    if height > 180:
        sum = sum + height
        count += 1

avg = sum / float(count)

print(sum,avg)
