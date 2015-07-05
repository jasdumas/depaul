'''
Can we read in a string line in a file with numbers
converted to a int and appened them back into a list
'''

infile = open('data1.txt')
line = infile.readline() # read line
values = line.split() # split line into a list
lst = [] # NULL list
print(values)
for value in values:
    lst.append(int(value))

print(lst)
