#  c-4 Employee Payroll Analysis
basic = float(input("Enter basic pay: "))
allowance = basic * 0.20
gross = basic + allowance

tax = gross * 0.10 if gross > 40000 else 0
net = gross - tax

print("Gross Salary:", gross)
print("Tax Deducted:", tax)
print("Net Salary:", net)