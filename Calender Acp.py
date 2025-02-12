print("\033c")

import calendar

print("Enter the Year and Month to see the Calendar of that Year and Month!")

yy = int(input("Enter the year: "))
mm = int(input("Enter the month in integer value: "))

month = calendar.month(yy, mm)

print(month)