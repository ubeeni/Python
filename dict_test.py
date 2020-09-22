# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 15:57:06 2020

@author: yubin
"""
dhash = {}
fp = open("data_log.csv","r",encoding="UTF8")
for line in fp:
    line = line.strip("\r\n")
    psd = line.split(",")
    query = psd[1]

    if not query in dhash:
        dhash[query] = 0
        
    dhash[query] += 1 
    
fp.close()

for query in dhash:
    print(query,dhash[query])