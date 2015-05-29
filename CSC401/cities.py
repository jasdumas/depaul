'''
While - indefinite loop
write a function that prompts the user to enter cities and appends to a list
and stops when a null string is entered/just hiting enter
'''

def cities():
    lst = []

    city = input("Enter a city (NULL to stop): ")

    while city != '':
        lst.append(city)
        city = input("Enter a city (NULL to stop): ")

    return lst

print(cities())
