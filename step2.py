# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 13:55:34 2020

@author: yubin
"""
fp = open("data_score.csv", 'r', encoding='UTF8')

sum = 0
count = 0
for line in fp:
    line = line.strip("\r\n")
    psd = line.split(",")
    name = psd[0]
    man = psd[1]
    height = psd[2]
    
    if man == "1":
        sum = sum + float(height)
        count += 1
    
avg = sum / float(count)
    
fout = open("result.txt", "w")
fout.write(str(avg))
fout.close()