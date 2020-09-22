# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 20:12:52 2020

@author: yubin
"""

import statpy as sp

fp = open("data.csv", "r", encoding='UTF8')

list_man = []

for line in fp:
    line = line.strip("\r\n")
    psd = line.split(",")
    #name = psd[0]
    man = psd[1]
    height = psd[2]
    
    if man == "1":
        list_man.append(float(psd[2])) 
           
avg = sp.DiscStat()
std = sp.DiscStat()

print("man_avg = %.2f"%(avg.get_avg(list_man)))
print("man_std = %.2f"%(std.get_std(list_man)))
