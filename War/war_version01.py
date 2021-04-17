"""
War (also known as Battle in the United Kingdom) is a simple card game, 
typically played by two players using a standard playing card deck — and often played by children. 
There are many variations, including the German 32-card variant Tod und Leben ("Life and Death").
Card rank (highest first): A K Q J 10 9 8 7 6 5 4 3 ...
Cards: 52
Players: 2
Skills required: Counting and card values
"""


# version one 

# we have four suits but for the game suits don't matter
# the deck has 52 cards
# each suit has 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14
# where J:11, Q:12, K:13, A:14

import random

# this version cards will be all numerical

# create a deck of cards with no suits
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4

# shuffle a deck
random.shuffle(deck) 

# just give half deck each 52 / 2 = 26 card each
player1_hand = deck[:len(deck)//2]
player2_hand = deck[len(deck)//2:]

print(len(deck))
print(deck)
player1_score = 0
player2_score = 0

while (len(player1_hand)>0) or (len(player2_hand)>0):

    # pop one card each
    player1_card = player1_hand.pop(0)
    player2_card = player2_hand.pop(0)
    print("~" * 40)
    input("\n1, 2, 3... War : Hit Enter")
    print(f"Player One : {player1_card}   and  Player Two : {player2_card}")
    if player1_card > player2_card:
        print("Player One Wins!")
        player1_score +=1
    elif player2_card > player1_card:
        print("Player Two Wins!")
        player2_score +=1
    else:
        print("It's a Draw")

    print(f"\nPlayer One Score: {player1_score}   and  Player Two Score: {player2_score}")

print("\n\n")
print("~" * 40)
print("Final Score")
print(f"Player One Score: {player1_score}   and  Player Two Score: {player2_score}")