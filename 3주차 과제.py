# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 14:42:44 2020

@author: yubin
"""
fp = open("data.csv", "r", encoding='UTF8')

sum1 = 0
count1 = 0
v1 = 0

sum2 = 0
count2 = 0
v2 = 0

for line in fp:
    line = line.strip("\r\n")
    psd = line.split(",")
    name = psd[0]
    man = psd[1]
    height = psd[2]
    
    if man == "1":
        sum1 = sum1 + float(height)
        v1 = v1 + float(height)**2
        count1 += 1
        
    elif man == "0":
        sum2 = sum2 + float(height)
        v2 = v2 + float(height)**2
        count2 += 1
        
avg1 = sum1 / float(count1)
dev1 = v1/float(count1)-avg1**2
avg2 = sum2 / float(count2)
dev2 = v2/float(count2)-avg2**2

fout = open("result.txt", "w")
fout.write("MAN\t%.2f\t%.2f\n"%(avg1,dev1))
fout.write("WOMAN\t%.2f\t%.2f\n"%(avg2,dev2))
fout.close()