
def rfib(n):
    if n <= 2:
        return 1
    return rfib(n-1) + rfib(n-2)
