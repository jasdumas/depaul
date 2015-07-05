# Price is Right Game

A = eval(input("Player A - Guess a number: "))
B = eval(input("Player B - Guess a number: "))
C = eval(input("Game Host - Enter the actual price: "))


if abs(C - A)  <  C - B and A < C: #If the diff. of C - A is less than C - B, then A is closer
    print("A's Guess: ", A, "\nB's Guess: ", B, "\nThe winner is: player A")
elif A > C and B > C:  #Scenario: Both players guess over the actual price
    print("No winner!")
elif A > C and B <= C: #Scenario: A's guess is over the actual price
    print("A's Guess: ", A, "\nB's Guess: ", B, "\nThe winner is: player B")
elif B > C and A <= C:  #Scenario: B's guess is over the actual price
    print("A's Guess: ", A, "\nB's Guess: ", B, "\nThe winner is: player A")
else: 
    print("A's Guess: ", A, "\nB's Guess: ", B, "\nThe winner is: player B")

        


    

