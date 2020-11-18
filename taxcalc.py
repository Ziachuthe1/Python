def tax_calc (rate, amount):
    tax = rate * amount 
    return tax
r = input("Enter the tax rate in decimal:")
a = input("enter the amount:")

print(tax_calc(float(r),float(a)))