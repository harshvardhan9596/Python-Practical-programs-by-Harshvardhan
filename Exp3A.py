# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 13:12:56 2026

@author: Harshvardhan Gaikwad
"""
n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
  for j in range(1, i + 1):
     print(j, end=" ")
  print()