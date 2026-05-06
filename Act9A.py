# -*- coding: utf-8 -*-
"""
Created on Fri May  1 22:37:08 2026

@author: Ashish Gaikwad
"""
import math

# Inputs
P = float(input("Enter loan amount: "))
R = float(input("Enter annual interest rate (%): "))
T = float(input("Enter time (in years): "))

# Convert to monthly
r = R / (12 * 100)
n = T * 12

# EMI formula
EMI = P * r * (math.pow(1 + r, n)) / (math.pow(1 + r, n) - 1)

print("Monthly EMI =", round(EMI, 2))
