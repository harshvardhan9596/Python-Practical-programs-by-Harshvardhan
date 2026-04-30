# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 15:33:44 2026

@author: Agce
"""
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self, bonus):
        total = self.salary + bonus
        print(f"Employee: {self.name}")
        print("Total Salary (with bonus):", total)


# Example usage
emp = Employee("Harshvardhan", 30000)
emp.calculate_salary(5000)
