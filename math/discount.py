purchase_amount = float(input("Enter the amount payed"))

if purchase_amount <= 1000:
    discount = 0.1 #discount is 10%
elif purchase_amount <= 500:
    discount = 0.05 #discount 5%
else:
    discount = 0 #no discount
final_price = purchase_amount * (1 - discount)
print ("price is :", final_price)
