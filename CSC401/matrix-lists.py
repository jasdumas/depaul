'''
Matrix - addition
'''


s = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
t = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]

nrows = len(s)
ncols = len(s[0])
sumit = [[0 for j in range(ncols)]for i in range(nrows)] # functional statement
# creates a matrix space to add to for s and t

for i in range(nrows):
    for j in range(ncols):
        sumit[i][j] = s[i][j] + t[i][j]

print(sumit)
        
