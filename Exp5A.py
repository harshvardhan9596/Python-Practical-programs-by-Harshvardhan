# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 12:57:31 2026

@author: harshvardhan Gaikwad
"""
student = {}
student["name"] = "Rahul"
student["age"] = 20
student["course"] = "Python"
print("Dictionary after adding elements:")
print(student)
student["age"] = 21
print("\nDictionary after updating a value:")
print(student)
del student["course"]
print("\nDictionary after deleting a key-value pair:")
print(student)
