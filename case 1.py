#  c-1 Progressive Electricity Billing
units = int(input("Enter units consumed: "))

if units <= 100:
    bill = units * 3.0
elif units <= 300:
    bill = (100 * 3.0) + ((units - 100) * 5.0)
else:
    bill = (100 * 3.0) + (200 * 5.0) + ((units - 300) * 8.0)

print("Total Electricity Bill: Rs.", bill)