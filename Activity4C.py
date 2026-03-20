"""
Created on Fri Mar 20 07:45:28 2026

@author: Harshvardhan Gaikwad
"""
# Program to remove duplicate mobile numbers from a contact list

# List of mobile numbers (with duplicates)
numbers = [9876543210, 9123456780, 9876543210, 9988776655, 9123456780, 9988776655]

# Removing duplicates using set()
unique_numbers = list(set(numbers))

# Displaying results
print("Original contact list:", numbers)
print("Contact list after removing duplicates:", unique_numbers)
