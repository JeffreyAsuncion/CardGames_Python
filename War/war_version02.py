"""
War (also known as Battle in the United Kingdom) is a simple card game, 
typically played by two players using a standard playing card deck — and often played by children. 
There are many variations, including the German 32-card variant Tod und Leben ("Life and Death").
Card rank (highest first): A K Q J 10 9 8 7 6 5 4 3 ...
Cards: 52
Players: 2
Skills required: Counting and card values
"""


# version two 

# add draw game play
# I, declare, war 3card deal
# 4th card compare

# 1. compare function
# 2. player score changed to cards left
# 3. draw game play

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

while (player1_hand) or (player2_hand):
    if (len(player1_hand) < 3) or (len(player2_hand) < 3):
        break 
    # pop one card each
    player1_card = player1_hand.pop(0)
    player2_card = player2_hand.pop(0)
    print("~" * 40)
    input("\n1, 2, 3... War : Hit Enter")
    # print("\n1, 2, 3... War : Hit Enter")
    print(f"Player One : {player1_card}   and  Player Two : {player2_card}")
    if player1_card > player2_card:
        print("Player One Wins!")
        player1_hand.extend([player1_card, player2_hand])
        
    elif player2_card > player1_card:
        print("Player Two Wins!")
        player2_hand.extend([player1_card, player2_hand])

    else:
        print("It's a Draw")
        # need to add game logic in case of a tie
        # draw = []
        # for i in range(4):
        #     if player1_hand:
        #         draw.append(player1_hand.pop(0))        
        #     if player2_hand
        #         draw.append(player2_hand.pop(0))
        # # print("\n1, 2, 3... War : Hit Enter")
        # print(f"Player One : {draw[3]}   and  Player Two : {draw[7]}")
        # if draw[3] > draw[7]:
        #     print("Player One Wins!")
        #     player1_hand.extend(draw)
            
        # elif draw[3] < draw[7]:
        #     print("Player Two Wins!")
        #     player2_hand.extend(draw)



    print(f"\nPlayer One Cards Left: {len(player1_hand)}   and  Player Two Cards Left: {len(player2_hand)}")

print("\n\n")
print("~" * 40)
print("Final Score")
print(f"\nPlayer One Cards Left: {len(player1_hand)}   and  Player Two Cards Left: {len(player2_hand)}")