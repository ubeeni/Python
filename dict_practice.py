# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 14:36:02 2020

@author: yubin
"""

dhash = {}
dhash["송혜교"] = 1
print(dhash["송혜교"])

dhash["송혜교"] += 1
print(dhash["송혜교"])

if "송혜교" in dhash:
    print("있음")
else:
    print("없음")

if not "송중기" in dhash:
    print("송중기 없음")
