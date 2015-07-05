def partition(soccer):
    new = soccer.split()  # split string into seperate entities in a list
    print(new)  # print list
    for name in new: # for loop to check each name in the list
        if name[0] >= 'A' and name[0] <= 'M':
            print('Group 1: ', name)
        else:
            print('Group 2: ', name)


list1 = '''Adam Drew Steve Mike Frank Zeke Alan Jeremy'''  # string of names
print(partition(list1))   # applies function to string of names
