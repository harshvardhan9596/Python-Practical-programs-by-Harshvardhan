# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 02:38:38 2026

@author: Harshvardhan Gaikwad
"""
with open("attendance.txt", "a") as f:
    for i in range(3):
        name = input("Enter student name: ")
        status = input("Present/Absent: ")
        f.write(name + " - " + status + "\n")

print("Attendance recorded successfully.")
