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

end_game = False


def starting_cards():
    new_card = random.choice(cards)
    user_cards.append(new_card)
    new_card = random.choice(cards)
    computers_cards.append(new_card)
    new_card = random.choice(cards)
    user_cards.append(new_card)

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

def player_blackjack(user_score, computer_score):
    if user_score == 21:
        print("You have blackjack. You win! ")
        end_game = True
        return end_game
    elif computer_score == 21:
        print("The computer has blackjack. You lose! ")
        end_game = True
        return end_game
    else:
        end_game = False
        return end_game

def over_21(player_cards, score):
    if score > 21:
        for i in range(len(player_cards)):
            if player_cards[i] == 11:
                print("You have an ace.")
                player_cards[i] = 1
                print(player_cards)
        new_score = add_cards(player_cards)
        if new_score > 21:
            print(f"Game over, you are bust, with a score of {new_score}! ")
            return True
        else:
            print(f"With ace being 1, your new score is {new_score}")
            if new_score == 21:
                print("Congratulations you got blackjack! You win! ")
                return True
            else:
                return False
    else:
        return False

          
def user_turn(user_cards, computers_cards):
    user_score = add_cards(user_cards)
    computer_score = add_cards(computers_cards)
    print(f"Your cards are: {user_cards}, which have a score of {user_score}.\n\nThe computers cards are: {computers_cards}, with a score of {computer_score} \n")
    
    is_blackjack = player_blackjack(user_score=user_score, computer_score=computer_score) #is_blackjack will become true if the game should end.
    if is_blackjack == True:
        return True, user_score, computer_score
    elif over_21(user_cards, user_score) == True:
        return True, user_score, computer_score
    else:
        users_turn = str(input("Do you want another card, Y or N "))
        if users_turn == "N":
            return True, user_score, computer_score
        elif users_turn == "Y":
            return False, user_score, computer_score
        else:
            print("Wrong response you lose! ")
            return True, user_score, computer_score

def got_ace(player_cards):
    for i in range(len(player_cards)):
        if player_cards[i] == 11:
            player_cards[i] = 1
            return True, player_cards
    return False, player_cards

# ==================================================== MAIN GAME RUNNING ====================================================

while True:
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = []
    computers_cards = []

    play_game = input("Welcome to blackjack, would you like to play a game? Enter 'Y' or 'N'. ")

    if play_game == "N":
        print("Thank you, come back soon.")
        break
    else:
        starting_cards()
        while True: 
            end_game, user_score, computer_score = user_turn(user_cards=user_cards, computers_cards=computers_cards)
            if end_game:
                break
            else:
                generate_card(user_cards)

        while True:
            computer_score = add_cards(computers_cards)
            ace, computers_cards = got_ace(computers_cards)
            
            if computer_score < 17:
                generate_card(computers_cards)
            elif computer_score > 21 and not ace:
                print(f"Computer score is {computer_score}, they are bust. You win! ")
                break
            elif computer_score > 21 and ace:
                computer_score = add_cards(computers_cards)
                if computer_score > 21:
                    print(f"Computer is bust with {computer_score}. You win! ")
                    break
            elif 17 <= computer_score <= 21:
                print(f"The computer score is {computer_score}")
                break

        if user_score > 21:
            print(f"Your score is {user_score}, which is over 21. You are bust, you lose!")
        elif computer_score > 21:
            print(f"Computer score is {computer_score}, which is over 21. Computer is bust, you win!")
        elif user_score > computer_score:
            print(f"Your score is {user_score}, the computer score is {computer_score}. You have the higher score, you win!")
        elif user_score < computer_score:
            print(f"Your score is {user_score}, the computer score is {computer_score}. You have the lower score, you lose!")
        elif user_score == computer_score:
            print(f"Your score is {user_score}, the computer score is {computer_score}. It's a draw!")
