from game_data import data
from art import logo, vs
import random
import os  
# Choose random person A and Choose random person B. 

# Display and compare person A and person B on screen.

# User guesses who has more followers

# Determine who has more followers and compare with the user guess. 

# Clear screen each time and add score up each correct guess.

# If wrong clear and display final score. 

def user_guess():
    global guess
    if input("Who has more followers? Type 'A' or 'B': ") == 'A':
        guess = 0
        return guess
    elif input("Who has more followers? Type 'A' or 'B': ") == 'B':
        guess = 1
        return guess


def most_followers(person_A, person_B):
    global winner
    if person_A['follower_count'] > person_B['follower_count']:
        winner = 0
        return winner
    else:
        winner = 1
        return winner


def compare_guess(guess, winner):
    global score
    global game_playing
    if guess == winner:
        print("You guessed correctly.")
        score += 1
        return score
    elif guess != winner:
        print("You guessed wrong.")
        game_playing = False
        return game_playing


def game():
    while game_playing == True:
        person_A = random.choice(data)
        person_B = random.choice(data) 
        print(logo)
        if score > 0:
            print(f"You're right! Current score: {score}")
        print(f"Compare A: {person_A['name']}, {person_A['description']}, {person_A['country']}. ")  
        print(vs)
        print(f"Compare B: {person_B['name']}, {person_B['description']}, {person_B['country']}. ")  
        
        winner = most_followers(person_A=person_A, person_B=person_B)
        guess = user_guess()
        compare_guess(guess=guess, winner=winner)
        os.system('cls')

    
# =========== MAIN ============
# Choose random persons, and store data in variable.


guess = ''
winner = ''
score = 0

game_playing = True


game(guess=guess, winner=winner)




