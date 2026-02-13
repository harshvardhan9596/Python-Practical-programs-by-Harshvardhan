year = int(input("Enter Year:"))
if(year %400 == 0)or(year %4 == 0 and year %100 != 0):
    print("The Year is Leap Year.")
else:
    print("The Year is not a leap year")
