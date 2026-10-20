#  c - 38 ATM Menu Simulation
balance = 5000.0

print("1. Check Balance\n2. Deposit\n3. Withdraw")
choice = int(input("Enter choice (1-3): "))

if choice == 1:
    print("Balance:", balance)
elif choice == 2:
    dep = float(input("Enter deposit amount: "))
    balance += dep
    print("New Balance:", balance)
elif choice == 3:
    wit = float(input("Enter withdrawal amount: "))
    if wit <= balance:
        balance -= wit
        print("New Balance:", balance)
    else:
        print("Insufficient funds!")