#  c-15 Smart Parking Fee
hours = int(input("Enter parking duration in hours: "))
vehicle_type = input("Enter vehicle type (Bike/Car): ").lower()

rate = 10 if vehicle_type == "bike" else 20
total_fee = hours * rate

print("Total Parking Fee: Rs.", total_fee)