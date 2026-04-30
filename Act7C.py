# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 15:32:20 2026

@author: Agce
"""
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            grade = "A"
        elif self.marks >= 75:
            grade = "B"
        elif self.marks >= 50:
            grade = "C"
        else:
            grade = "Fail"

        print(f"Student: {self.name}")
        print("Grade:", grade)


# Example usage
stu = Student("Harshvardhan", 82)
stu.calculate_grade()