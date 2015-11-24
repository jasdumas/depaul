'''
For example ORFunction([[True, False], [False, False]], [[False, True], [True, False]])
should return [[True, True], [True, False]]. 
And ORFunction([[True, False, True], [False, False, True]], [[False, True], [True, False]]) 
should return an error message.

'''
import numpy as np
mat1 = np.array([[True, False], [False, False]])
mat2 = np.array([[False, True], [True, False]])
mat3 = np.array([[True, False, True], [False, False, True]])
mat6 = np.array([[True, False, True], [True, False, True]])
mat4 = np.array([[False, True], [True, False]])
mat5 = mat1 + mat2 # function should match this output

def ORFunction(mat1, mat2):
    lst = []
    lst2 =[]
    if mat1.shape != mat2.shape:
        return "These boolean matricies cannot be combined because they are not the same shape"
    for i in mat1:
        for boolval in i:
            #print(boolval)
            lst.append(boolval)   
    for x in mat2:
        for boolval2 in x:
            #print(boolval2)  
            lst2.append(boolval2)        
    for index in range(0, len(lst)):
        print(lst[index] or lst2[index])
        

ORFunction(mat1, mat2)

