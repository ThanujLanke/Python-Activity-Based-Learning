#  c - 58 Library Fine Calculator
allowed_days = 14
actual_days = int(input("Enter total days kept: "))

if actual_days > allowed_days:
    fine = (actual_days - allowed_days) * 5
    print("Book is overdue. Fine to pay: Rs.", fine)
else:
    print("Book returned on time. No fine!")