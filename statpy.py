# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 19:53:17 2020

@author: yubin
"""

import numpy as np

class DiscStat:
    def get_avg(self, list_data):
        sum = 0
        for td in list_data:
            sum += td
        return float(sum) / len(list_data)
    
    def get_std(self, list_data):
        avg = self.get_avg(list_data)
        ssum = 0
        for td in list_data:
            ssum += td*td
        dev = float(ssum) / len(list_data) - avg*avg
        return np.sqrt(dev)
    
class TestStat:
    name = "Test Statistics"
    def t_test(self):
        return "t_test"
    def get_name(self):
        return self.name
    
if __name__ == "__main__":
    list_data = [100,200,300]
    da = DiscStat()
    print(da.get_std(list_data))