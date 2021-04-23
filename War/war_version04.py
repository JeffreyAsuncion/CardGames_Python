"""
War (also known as Battle in the United Kingdom) is a simple card game, 
typically played by two players using a standard playing card deck — and often played by children. 
There are many variations, including the German 32-card variant Tod und Leben ("Life and Death").
Card rank (highest first): A K Q J 10 9 8 7 6 5 4 3 ...
Cards: 52
Players: 2
Skills required: Counting and card values
"""
# version four
# 1. encapsulate the code into function for efficiency and reability 


import random
from clrprint import *

def compare_values(player1_strA, player2_strA, player1_card, player2_card, player1_hand, player2_hand, spoils):
    if player1_card > player2_card:
        print("\tPlayer One Wins!")
        # winner collects spoils
        player1_hand += spoils
    elif player2_card > player1_card:
        print("\tPlayer Two Wins!")
        # winner collects spoils
        player2_hand += spoils
    else:
        # check which player has enough cards to play draw hand
        if len(player1_hand) < 4:
            #player 2 wins this round
            print("\n player 1 : out of cards")
            # spoils go to player2
            player2_hand += spoils
            return
        if len(player2_hand) < 4:
            # player 1 wins this round
            print("\n player 2 : out of cards")
            # spoils go to player1
            player1_hand += spoils
            return
        # Draw_function
        draw_func(player1_hand, player2_hand, spoils)


def draw_func(player1_hand, player2_hand,spoils):
    # need to add game logic in case of a tie
    p1_1 = player1_hand.pop(0)
    p1_2 = player1_hand.pop(0)
    p1_3 = player1_hand.pop(0)
    player1_strA = str(player1_hand.pop(0))

    p2_1 = player2_hand.pop(0)
    p2_2 = player2_hand.pop(0)
    p2_3 = player2_hand.pop(0)
    player2_strA = str(player2_hand.pop(0))
    input()
    print("\tI\tI")
    print(f"\t{p1_1}\t{p2_1}")
    
    input()
    print("\tDECLARE\tDECLARE")
    print(f"\t{p1_2}\t{p2_2}")
    input()
    print("\tWAR\tWAR")
    print(f"\t{p1_3}\t{p2_3}")
    input()
    print("\tDraw Battle")

    # this catches the empty pop
    player1_str = player1_strA[1:]
    player2_str = player2_strA[1:]
    
    player1_card = dict[player1_str]
    player2_card = dict[player2_str]
    # where ever pop is compare need to paste this

    spoils = spoils + [p1_1, p1_2, p1_3, player1_strA, p2_1, p2_2, p2_3, player2_strA]

    compare_values(player1_strA, player2_strA, player1_card, player2_card, player1_hand, player2_hand, spoils)
    

def card_to_value(player1_hand, player2_hand):
    # pop one card eachprint(deck1)
    player1_strA = str(player1_hand.pop(0))
    player2_strA = str(player2_hand.pop(0))

    player1_str = player1_strA[1:]
    player2_str = player2_strA[1:]
    
    player1_card = dict[player1_str]
    player2_card = dict[player2_str]
    
    return (player1_card, player2_card, player1_strA, player2_strA)


dict = { 
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}

deck = []
# unicode for the card suits `very cool stuff`
suit = ['\u2666', '\u2665', '\u2660', '\u2663']
cards = ['2','3','4','5','6','7','8','9','10', 'J', 'Q', 'K', 'A']
for symbol in suit:
    for card in cards:
        deck.append(symbol+card)

# shuffle a deck
random.shuffle(deck) 
random.shuffle(deck)
# just give half deck each 52 / 2 = 26 card each
player1_hand = deck[:len(deck)//2]
player2_hand = deck[len(deck)//2:]

# print(len(deck))
# print(deck)
i = 1

while player1_hand and player2_hand:
    # # show hands
    clrprint(player1_hand, clr='blue')
    clrprint(player2_hand, clr='green')

    player1_card, player2_card, player1_strA, player2_strA = card_to_value(player1_hand, player2_hand)

    print("~" * 40)
    print(f"Round {i}")
    i += 1
    input("\n1, 2, 3... War : Hit Enter")
    print(f"\nPlayer One   and  Player Two")
    print(f"\t{player1_strA}\t\t{player2_strA}")
    
    spoils = [player1_strA, player2_strA]
    compare_values(player1_strA, player2_strA, player1_card, player2_card, player1_hand, player2_hand, spoils)
    print(f"\nPlayer One(# of cards): {len(player1_hand)}   and  Player Two(# of cards): {len(player2_hand)}  total cards {len(player1_hand)+len(player2_hand)}")

print("\n\n" + "~" * 40)
print("Final Score")
print(f"\nPlayer One(# of cards): {len(player1_hand)}   and  Player Two(# of cards): {len(player2_hand)}  total cards {len(player1_hand)+len(player2_hand)}")