# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 02:33:45 2026

@author: Harshvardhan Gaikwad
"""
with open("expenses.txt", "w") as f:
    for i in range(5):
        amt = float(input(f"Enter expense for day {i+1}: "))
        f.write(str(amt) + "\n")
total = 0
with open("expenses.txt", "r") as f:
    for line in f:
        total += float(line.strip())
print("Total Monthly Expense:", total)
