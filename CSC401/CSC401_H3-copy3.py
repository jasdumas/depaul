def payRoll(money):
   return money[0] * money[1]   
        
ask = eval(input("Enter your hourly wage and hours worked as a list: "))  
### User has to enter [wage, hours] with brackets
print(ask)

if ask[0] > 0 and ask[1] > 0:
    value = payRoll(ask)
if ask[0] <= 0 or ask[1] <= 0:
    print("STOP")  
if payRoll(ask) > 400 and ask[1] > 40: # over 400 and overtime
    tax = 0.28
    actual = ask[0] * 40
    otHours = ask[1] - 40
    newWage = ask[0] * 1.5
    overtime = otHours * newWage
    netPay = actual + overtime
    wTax = netPay * tax  
    plusTax = netPay - wTax
    print("Here is your take home pay with a tax rate of 28 %: ", "$",plusTax)
elif ask[0] * ask[1] <= 400 and ask[1] > 40: # under 400 overtime
    tax = 0.20
    actual = ask[0] * 40
    otHours = ask[1] - 40
    newWage = ask[0] * 1.5
    overtime = otHours * newWage
    netPay = actual + overtime
    wTax = netPay * tax  
    plusTax = netPay - wTax
    print("Here is your take home pay with a tax rate of 20 %: ", "$",plusTax)


if payRoll(ask) > 400 and ask[1] <= 40: # over 400 no overtime
    tax = 0.28    
    wTax = value * tax  
    plusTax = abs(wTax - value)
    print("Here is your take home pay with a tax rate of 28 %: ", "$",plusTax)
elif ask[0] * ask[1] <= 400 and ask[1] <= 40: # under 400 no overtime
    tax = 0.20    
    wTax = value * tax  
    plusTax = abs(wTax - value)
    print("Here is your take home pay with a tax rate of 20 %: ", "$",plusTax)

