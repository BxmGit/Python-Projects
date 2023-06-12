############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from art import logo

def starting_cards():
    new_card = random.choice(cards)
    user_cards.append(new_card)
    new_card = random.choice(cards)
    user_cards.append(new_card)
    new_card = random.choice(cards)
    computers_cards.append(new_card)


def generate_card(whos_card):
    new_card = random.choice(cards)
    whos_card.append(new_card)
    return whos_card

def generate_comp_cards():
    new_card = random.choice(cards)
    computers_cards.append(new_card)

def add_cards(whos_cards):
    score = 0 
    for x in whos_cards:
        score += x
    return score


print(logo)
play_game = input("Welcome to blackjack, would you like to play a game? Enter 'Y' or 'N'. ")
end_game = False

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
computers_cards = []

user_score = 0
computer_score = 0

# while end_game != True:
#     if play_game == "N":
#         print("Come back soon..!")
#         end_game = True
#     elif play_game == "Y":
#         print("Play game.")
#     # code




starting_cards()
print(user_cards)
print(computers_cards)

user_score = add_cards(user_cards)
print(user_score)
computer_score = add_cards(computers_cards)
print(computer_score)

input(f"Your cards are: {user_cards}, which have a score of {user_score}.\n\nThe computers cards are: {computers_cards}, with a score of {computer_score} \nWould you like another card? Y or N. ")

