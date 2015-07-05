hours = eval(input("Enter hours driven (> 0): "))
avSpeed = eval(input("Enter average speed (> 0): "))

# Formula is d = x*t where x is speed & t is time

if hours <= 0 or avSpeed <= 0:
    print("This is an invalid value, Please enter a positive value.")
else: print("Hours driven: " , hours , ", ",  "Average Speed: " , avSpeed,  " and Distance Traveled: ", (hours*avSpeed))



