# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 15:41:21 2026

@author: Harshvardhan Gaikwad
"""
class ATM:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        try:
            if amount > self.balance:
                raise ValueError("Insufficient balance ❌")
            
            self.balance -= amount
            print("Withdrawal successful ✅")
            print("Remaining Balance:", self.balance)

        except ValueError as e:
            print(e)


# Example
atm = ATM(1000)
atm.withdraw(1500)   # will show error
