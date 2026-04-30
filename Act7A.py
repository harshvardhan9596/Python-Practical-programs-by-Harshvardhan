# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 15:32:14 2026

@author: Harshvardhan Gaikwad
"""
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)
        print("Current Balance:", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance ❌")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)
            print("Current Balance:", self.balance)


# Example usage
acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(300)
