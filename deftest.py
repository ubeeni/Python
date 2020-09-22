# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 13:34:51 2020

@author: yubin
"""
def compute_avg(list_data):
    sum = 0
    for td in list_data:
        sum += td
    avg = sum / len(list_data)
    return avg

list_man = []
list_woman = []
fp = open("data.csv", "r", encoding='UTF8')
for line in fp:
    line = line.strip("\r\n")
    psd = line.split(",")
    man = psd[1]
    height = float(psd[2])
    if man == "1":
        list_man.append(height)
    elif man == "0":
        list_woman.append(height)
        
avg_man = compute_avg(list_man)
avg_woman = compute_avg(list_woman)

print(avg_man, avg_woman) 
