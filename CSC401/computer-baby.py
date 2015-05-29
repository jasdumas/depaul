def ageYears(y):
    return y * 12

ask = eval(input("Enter your age in years: "))

value = ageYears(ask)

if ask < 6:
    print("How did you learn how to use a computer, baby?")
else:
    print("Your months on earth:", value)
