# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 13:05:31 2026

@author: Harshvardhan Uday Gaikwad
"""
set1 = set(map(int, input("Enter elements of first set (space-separated): ").split()))
set2 = set(map(int, input("Enter elements of second set (space-separated): ").split()))
union_set = set1 | set2
intersection_set = set1 & set2
print("Union of the sets:", union_set)
print("Intersection of the sets:", intersection_set)
