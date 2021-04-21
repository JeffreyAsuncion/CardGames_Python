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
# if draw I declare war and compare 

# we have four suits but for the game suits don't matter
# the deck has 52 cards
# each suit has 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14
# where J:11, Q:12, K:13, A:14

import random

# this version cards will be all numerical
# H: heart 
# D: diamond
# C: clubs
# S: spades

deck1 = []
suit = ['D','H', 'S', 'C']
cards = ['2','3','4','5','6','7','8','9','10', 'J', 'Q', 'K', 'A']
for symbol in suit:
    for card in cards:
        # print(symbol + card)
        deck1.append(symbol+card)
# dictionary to match card to value


# deck1 will become deck

# store deck1[1:]

# create a deck of cards with no suits
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4

# shuffle a deck
random.shuffle(deck) 

# just give half deck each 52 / 2 = 26 card each
player1_hand = deck[:len(deck)//2]
player2_hand = deck[len(deck)//2:]

print(len(deck))
print(deck)
print(deck1)
player1_score = 0
player2_score = 0
draw_counter = 0
double_draw = False
i = 0

while player1_hand and player2_hand:

    # pop one card each
    player1_card = player1_hand.pop(0)
    player2_card = player2_hand.pop(0)

    print("~" * 40)
    print(f"Round {i}")
    i += 1
    input("\n1, 2, 3... War : Hit Enter")
    print(f"Player One : {player1_card}   and  Player Two : {player2_card}")
    
    # compare_cards
    if player1_card > player2_card:
        print("Player One Wins!")
        player1_score +=1
        # winner collects spoils
        player1_hand.extend([player1_card, player2_card])
    elif player2_card > player1_card:
        print("Player Two Wins!")
        player2_score +=1
        # winner collects spoils
        player2_hand.extend([player1_card, player2_card])
    else:
        print("It's a Draw")
        draw_counter += 1

        # check which player has enough cards to play draw hand
        # check len(player1_hand < 4)
        if len(player1_hand) <= 4:
            #player 2 wins this round
            print("\n\n\n")
            break
        if len(player2_hand) <= 4:
            # player 1 wins this round
            print("\n\n\n")
            break

        print("I DECLARE WAR")
        print("I DECLARE WAR")
        print("I DECLARE WAR")
        # need to add game logic in case of a tie
        p1_1 = player1_hand.pop(0)
        p1_2 = player1_hand.pop(0)
        p1_3 = player1_hand.pop(0)
        player1_card = player1_hand.pop(0)

        p2_1 = player2_hand.pop(0)
        p2_2 = player2_hand.pop(0)
        p2_3 = player2_hand.pop(0)
        player2_card = player2_hand.pop(0)

        spoils = [p1_1, p1_2, p1_3, player1_card, p2_1, p2_2, p2_3, player2_card]
        # compare_card
        print(f"Player One : {player1_card}   and  Player Two : {player2_card}")
        if player1_card > player2_card:
            print("Player One Wins!")
            player1_score +=1
            # winner collects spoils
            player1_hand.extend(spoils)
        elif player2_card > player1_card:
            print("Player Two Wins!")
            player2_score +=1
            # winner collects spoils
            player2_hand.extend(spoils)
        else:
            # Call Draw 
            double_draw = True


    print(f"\nPlayer One Score: {player1_score}   and  Player Two Score: {player2_score}")




print("\n\n")
print("~" * 40)
print("Final Score")
print(f"Player One Score: {player1_score}   and  Player Two Score: {player2_score}")
print(f"number of draws : {draw_counter} {double_draw}")
