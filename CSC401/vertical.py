'''
Recursion : Print/chop up a interger into its individual numbers

'''


def vertical(n):
    if n < 10:
        print(n)

    else:
        vertical(n // 10)   # 3124 divided by 10 = 312
        print(n % 10) # 10 goes into 312 with a remainder of 2

vertical(3124)
