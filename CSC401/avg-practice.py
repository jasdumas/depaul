def avg(value1, value2):
    average = (value1 + value2) / 2
    # print("The result is: ", average)  ### It also work not commented too! Let's see if removing this works also: it does!
    return average  ## this works

val1 = eval(input("Enter first value: "))
val2 = eval(input("Enter second value: "))
# print("Does this work: ", avg(val1, val2))  # Nope! You can only return a single print result
print("Does this work: ", avg(val1, val2)) ## this works
