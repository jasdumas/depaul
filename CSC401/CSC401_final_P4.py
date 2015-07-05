'''
CSC 401: Final Exam (take home)
Problem 4: Develop a class - 25pts
'''


class BankAccount:

    def __init__(self,initial = 0.00): # if nothing is entered the balance is 0
        self.s = float(initial)
    
    def withdraw(self, moneyOut):
        self.s = float(self.s - moneyOut) # redefines the new balance after taking money out

    def deposit(self, moneyIn):
        self.s = float(self.s + moneyIn)  # redefines the new balance putting money in

    def printBalance(self):
        print("The balance is $", self.s)
