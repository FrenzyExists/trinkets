# Personal income Tax Calculator (PR)

 = float(input("Insert your current income: "))
tax = 0

if income <= 9000:
    tax = 0
elif income <= 25000:
    tax = (income - 9000) * 0.07
elif  income <= 41500:
    tax = 1120 + (income - 25000) * 0.14
elif  income <= 61500:
    tax = 3430 + (income - 41500) * 0.25
else:
    tax = 8430 + (income - 61500) * 0.33
    
print (tax + income)