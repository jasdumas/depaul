def payRoll(money):
   return money[0] * money[1]
   
    
    
ask = eval(input("Enter your hourly wage and hours worked as a list: "))  
### User has to enter [wage, hours] with brackets
print("This is what you entered: ",ask)
value = payRoll(ask)

##if ask[0] > 0 and ask[1] > 0:
##   value = payRoll(ask)
##   print(value)
#if ask[0] <= 0 or ask[1] <= 0:
    #print("STOP")  # for debugging, will remove for final program  
##elif ask[1] > 40:  # if you worked more than 40 hours
##    otHours = abs(40 - ask[1]) # standard hours - extra hours = # OT Hours
##    overTime = otHours * (ask[0] * 1.5) # time and a half!
##    original = (ask[0] * 40) # standard wage * hours
##    print("You worked extra hours, here is your net pay: ", "$",original + overTime)
##if payRoll(ask) > 400: 
##    tax = 0.28
##    wTax = (original + overTime) * tax  
##    plusTax = abs(wTax - (original + overTime))
##    print("Here is your take home pay with a tax rate of 28 %: ", "$",plusTax)
if value > 400 and ask[1] < 40: ## over $400 but no overtime
    tax = 0.28
    wTax = tax * value
    plusTax = value - wTax
    print("Trial ", plusTax)
elif value > 400 and ask[1] > 40: ## over $400 with overtime
    tax = 0.28
    otHours = abs(40 - ask[1]) # standard hours - extra hours = # OT Hours
    overTime = otHours * (ask[0] * 1.5) # time and a half!
    original = (ask[0] * 40) # standard wage * hours
    wTax = (original + overTime) * tax  
    plusTax = abs(wTax - (original + overTime))
    print("Here is your take home pay with a tax rate of 28 %: ", "$",plusTax)
if value <= 400 and ask[1] < 40: ## under $400 with no overtime
    tax = 0.20    
    wTax = value * tax  
    plusTax = abs(wTax - value)
    print("Here is your take home pay with a tax rate of 20 %: ", "$",plusTax)
elif ask[0] * ask[1] <= 400 and ask[1] > 40:   ## under $400 with overtime
    tax = 0.20
    otHours = abs(40 - ask[1]) # standard hours - extra hours = # OT Hours
    overTime = otHours * (ask[0] * 1.5) # time and a half!
    original = (ask[0] * 40) # standard wage * hours
    wTax = (original + overTime) * tax  
    plusTax = abs(wTax - (original + overTime))
    print("Here is your take home pay with a tax rate of 20 %: ", "$",plusTax)



