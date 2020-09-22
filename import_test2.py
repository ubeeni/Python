# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 19:38:01 2020

@author: yubin
"""

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

x = np.array([0.3, 3.8, 1.2, 2.5])
y = np.array([11, 25, 9, 26])

ax.scatter(x, y, marker='^', color='darkgreen')
plt.show()