'''
CSC 401: Final exam
Problem 2: Recursion - 25pts
'''



s = "h e l l o"

length = len(s)
counter = 0

for i in range(0, length):
    if s[i] == " ":
        counter += 1

print("non-recursive: ", counter)
        

#####

def spaces(s):
    length = len(s)
    
    
    if length == 1: # base case
        return 0
    else:
        return (1 if s[0] == " " else 0) + spaces(s[1:])
        
        
print("recursive ",spaces(s))

