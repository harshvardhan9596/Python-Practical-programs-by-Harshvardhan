# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 15:51:16 2026

@author: Harshvardhan Gaikwad
"""
try:
    age = int(input("Enter your age: "))

    if age < 0 or age > 120:
        raise ValueError("Invalid age entered ❌")

    print("Registration successful ✅")

except ValueError:
    print("Please enter a valid number for age ❌")
