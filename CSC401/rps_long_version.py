'''
Rock - Paper - Scissors Function
Rules:
a. Rock always beats Scissors (rock dulls scissors)
b. Scissors always beats Paper (scissors cut paper)
c. Paper always beats Rock (paper covers rock)
'''
def rps(choice1, choice2):
            
    if choice1 == 'R' and choice2 == 'S':
        print("Player 1 is the round winner")
    elif choice1 == 'P' and choice2 == 'R':
        print("Player 1 is the round winner")
    elif choice1 == 'S' and choice2 == 'P':
        print("Player 1 is the round winner")
    elif choice1 == choice2:
        print("This is a tie round")
    else:
        print("Player 2 is the round winner")

keepPlaying = input("Would you like to play Rock, Paper, Scissors? (y to continue) ")
possibleResponses = ['y', 'Y', 'yes', 'Yes', 'OK']

player1Counter = 0
player2Counter = 0
gameTie = 0

while keepPlaying in possibleResponses:
    player1 = input("Player 1, enter R, P, S: ")
    player2 = input("Player 2, enter R, P, S: ")    
    keepPlaying = input("Do you still want to play? ")
    if player1 == 'R' and player2 == 'S':
        player1Counter += 1
        print(rps(player1, player2))
    elif player1 == 'P' and player2 == 'R':
        player1Counter += 1
        print(rps(player1, player2))
    elif player1 == 'S' and player2 == 'P':
        player1Counter += 1
        print(rps(player1, player2))
    elif player1 == player2:
        gameTie += 1
        print(rps(player1, player2))
    else:
        player2Counter += 1
        print(rps(player1, player2))

print("Player 1 won {} times\nPlayer 2 won {} times \nThere were {} ties.".format(player1Counter, player2Counter, gameTie))
    


