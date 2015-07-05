def payRoll(money):
   return money[0] * money[1]
   
    
    
ask = eval(input("Enter your hourly wage and hours worked as a list: "))  
### User has to enter [wage, hours] with brackets
print(ask)



if ask[0] > 0 and ask[1] > 0:
    value = payRoll(ask)
if ask[0] <= 0 or ask[1] <= 0:
    print("STOP")  # for debugging, will remove for final program
elif ask[1] > 40:  # if you worked more than 40 hours
    otHours = abs(40 - ask[1]) # standard hours - extra hours = # OT Hours
    overTime = otHours * (ask[0] * 1.5) # time and a half!
    original = (ask[0] * 40) # standard wage * hours
    print("You worked extra hours, here is your net pay: ", "$",original + overTime)
if payRoll(ask) > 400: 
    tax = 0.28    
    wTax = value * tax  
    plusTax = abs(wTax - value)
    print("Here is your take home pay with a tax rate of 28 %: ", "$",plusTax)
elif ask[0] * ask[1] <= 400: 
    tax = 0.20    
    wTax = value * tax  
    plusTax = abs(wTax - value)
    print("Here is your take home pay with a tax rate of 20 %: ", "$",plusTax)

