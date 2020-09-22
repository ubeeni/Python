# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 18:33:08 2020

@author: yubin
"""

def compute_avg(list_data):
    sum = 0
    for td in list_data:
        sum += td
    avg = float(sum) / len(list_data)
    return avg

def compute_max(list_data):
    first = 1
    for td in list_data:
        if first == 1:
            max = td
            first = 0
        if max < td:
            max = td
    return max

if __name__ == "__main__":
    list_test = [10,20,30]
    print(compute_avg(list_test))
    print(compute_max(list_test))