#  c-21Traffic Violation Penalty
offence = input("Enter offence (Helmet / Speeding / Drunk): ")
repeat = input("Is it a repeat offence? (yes/no): ")

fine = 500 if offence == "Helmet" else (1500 if offence == "Speeding" else 10000)
if repeat == "yes":
    fine *= 2

print("Total Penalty Fine: Rs.", fine)