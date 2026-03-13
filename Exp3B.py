# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 13:12:56 2026

@author: Harshvardhan Gaikwad
"""
def simple_interest(principal, rate, time):
  si = (principal * rate * time) / 100
  return si
p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time (in years): "))
interest = simple_interest(p, r, t)
print("Simple Interest is:", interest)