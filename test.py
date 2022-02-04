def add_tax(total):
    tax = total * 0.06
    new_total = tax + total
    return new_total

print(add_tax(100))

bills = [115, 120, 42]
 
new_bills = []
 
for i in range(len(bills)):
  total = add_tax(bills[i])
  new_bills.append("Total amount owed is $" + "{:.2f}".format(total) + ". Thank you! :)")
 
print(new_bills)

# This is just a test project