# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 14:51:14 2026

@author: Harshvardhan Gaikwad
"""
# file name
file_name = "expenses.txt"

# take input from user
date = input("Enter date (DD-MM-YYYY): ")
amount = float(input("Enter expense amount: "))

# store in file (append mode)
with open(file_name, "a") as file:
    file.write(f"{date},{amount}\n")

print("Expense saved successfully!")

total = 0

with open(file_name, "r") as file:
    for line in file:
        parts = line.strip().split(",")
        
        if len(parts) != 2:
            continue   # skip invalid lines
        
        date, amount = parts
        total += float(amount)

print("Total Monthly Expense:", total)