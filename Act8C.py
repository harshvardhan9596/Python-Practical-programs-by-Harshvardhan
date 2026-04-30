# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 15:51:31 2026

@author: Agce
"""
try:
    total_bill = float(input("Enter total bill: "))
    people = int(input("Enter number of people: "))

    amount_per_person = total_bill / people
    print("Each person should pay:", amount_per_person)

except ZeroDivisionError:
    print("Number of people cannot be zero ❌")

except ValueError:
    print("Invalid input ❌")
