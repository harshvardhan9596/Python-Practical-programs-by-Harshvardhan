# -*- coding: utf-8 -*-
"""
Created on Fri May  1 22:37:16 2026

@author: Ashish Gaikwad
"""
import math

# Input coordinates
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Distance formula
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("Distance =", round(distance, 2))
