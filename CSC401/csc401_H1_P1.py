price = eval(input("Enter a Price (> 0): "))
quant = eval(input("Enter a quantity (> 0): "))

if quant <= 0 or price <= 0:
    print("This is an invalid value, Please enter a positive value.")
elif type(quant) != type(1) or type(price) != type(1.0) : 
    print("This is an invalid value, Please enter a float and integer value, respectively.")
else: print("The total price is: $ " , (price*quant))    

