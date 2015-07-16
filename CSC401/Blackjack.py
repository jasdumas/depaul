import random

def shuffleDeck():

    suits = {'\u2660','\u2661','\u2662','\u2663'}
    ranks = {'2','3','4','5','6','7','8','9','10','J','Q','K','A'}
    deck = []

    for suit in suits:
        for rank in ranks:
            deck.append(rank + ' ' + suit)


    random.shuffle(deck)        # Now shuffle the deck

    return deck

def dealCard(deck):
    return deck.pop()


def total(hand):

    values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '1':10,
              'J':10, 'Q':10, 'K':10,'A':11}
    result = 0
    numAces = 0

    for card in hand:
        result += values[card[0]]      # 0th char is the rank
        if card[0] == 'A':
            numAces += 1

    while result > 21 and numAces >0:    # convert ace from 11 to 1
        result -= 10
        numAces -= 1

    return result


def compareHands(house,player):

    houseTotal = total(house)
    playerTotal = total(player)

    if houseTotal > playerTotal:
        print('You lose.')
    elif houseTotal < playerTotal:
        print('You win.')
    elif houseTotal == 21 and 2 == len(house) < len(player):
        print('You lose.')      # house wins with a blackjack
    elif playerTotal == 21 and 2 == len(player) < len(house):
        print('You win.')       # players wins with a blackjack
    else:
        print('A tie.')

def blackjack():
    deck = shuffleDeck()
    house = []
    player = []

    for i in range(2):
        player.append(dealCard(deck))
        house.append(dealCard(deck))

    print('House: {}  {}'.format(house[0], house[1]))
    print('  You: {}  {}'.format(player[0], player[1]))

    answer = input("Hit or stand? (default: hit): ")

    while answer in {'', 'h', 'hit'}:
        card = dealCard(deck)
        player.append(card)
        print('You got {}'.format(card))

        print(player)
        
        if total(player) > 21:
            print('You went over... You lose.')
            return

        answer = input('Hit or stand? (default: hit): ')


    while total(house) < 17:
        card = dealCard(deck)
        house.append(card)
        print('House got {}'.format(card))

        print(house)

        if total(house) > 21:
            print('House went over... You win.')
            return

    compareHands(house,player)


blackjack()
