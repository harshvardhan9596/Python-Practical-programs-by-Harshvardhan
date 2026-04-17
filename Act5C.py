# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 13:26:23 2026

@author: Harshvardhan Gaikwad
"""
purchases = ["apple", "banana", "apple", "orange", "banana", "apple"]
frequency = {}
for item in purchases:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1
print("Item frequency:", frequency)