# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 02:57:52 2026

@author: Harshvardhan Gaikwad
"""
try:
    with open("complaints.txt", "r") as file:
        print("List of Complaints:\n")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Complaint file not found.")