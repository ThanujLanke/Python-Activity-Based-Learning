# c - 24Courier Charge Calculator
weight = float(input("Enter parcel weight in kg: "))
urgent = input("Is it urgent? (yes/no): ")

rate = 50 if weight <= 5 else 100
total = weight * rate

if urgent == "yes":
    total += 200

print("Total Courier Charges: Rs.", total)