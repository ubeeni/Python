# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 19:57:31 2020

@author: yubin
"""

import statpy as sp

ds = sp.DiscStat()
ts = sp.TestStat()

print(ds.get_avg())
print(ts.t_test())