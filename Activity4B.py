"""
Created on Fri Mar 20 07:45:28 2026

@author: Harshvardhan Gaikwad
"""
# Taking prices from user

prices = []

n = int(input("Enter number of products: "))

for i in range(n):
    price = int(input("Enter price: "))
    prices.append(price)

total_bill = sum(prices)

print("Total bill amount:", total_bill)