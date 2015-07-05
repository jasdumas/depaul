def positiveInt(value):
    vallist = list(range(10, 0, -1))
    
    for num in vallist:
        if value % num == 0:
            print(num)
        else:
            print('Nope')

print(positiveInt(10))
