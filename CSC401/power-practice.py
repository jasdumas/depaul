'''
power() calculates iteratively
powerrec() calculates recursively (but slowly)

'''

def power(a,n):
    res = 1
    for i in range(n):
        res *= a
    return res

def powerrec(a,n):
    if n == 0:
        return 1
    else:
        return a*powerrec(a,n-1)

def rpower(a,n): ## number of calculations is very small = log(n)
    if n == 0:
        return 1

    tmp = rpower(a, n//2)

    if n % 2 == 0:   ## is that even? Remainder = 0 is even, or 1 for odd
        return tmp * tmp
    else:
        return a * tmp * tmp 
        
