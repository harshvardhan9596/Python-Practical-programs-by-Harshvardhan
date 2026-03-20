"""
Created on Fri Mar 20 07:34:01 2026

@author: Harshvardhan Gaikwad
"""
marks = [78, 85, 90, 67, 88]
total = sum(marks)

#length of students
count = len(marks)

# Calculating average
average = total / count

# Finding topper marks (maximum marks)
topper = max(marks)

# Displaying the results
print("Marks of students:", marks)
print("Average marks:", average)
print("Topper marks:", topper)
