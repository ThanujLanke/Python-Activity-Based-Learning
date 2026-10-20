#  c - 6 Railway Fare Calculator
distance = int(input("Enter distance in km: "))
age = int(input("Enter passenger age: "))

base_fare = distance * 1.5
if age < 12 or age > 60:
    base_fare = base_fare * 0.75  # 25% discount

print("Final Railway Fare: Rs.", base_fare)


