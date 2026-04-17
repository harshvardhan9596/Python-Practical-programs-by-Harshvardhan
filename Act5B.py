# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 13:25:42 2026

@author:Harshvardhan Gaikwad
"""
# Roll numbers of students in two classes
class_A = {101, 102, 103, 104, 105}
class_B = {104, 105, 106, 107}

# Find students present in both classes
common_students = class_A.intersection(class_B)

# Output
print("Students present in both classes:", common_students)