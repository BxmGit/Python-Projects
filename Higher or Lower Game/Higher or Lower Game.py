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
    guess = input("Who has more followers? Type 'A' or 'B': ")
    if guess == 'A':
        return 0
    elif guess == 'B':
        return 1


def most_followers(person_A, person_B):
    if person_A['follower_count'] > person_B['follower_count']:
        return 0
    else:
        return 1


def compare_guess(guess, winner):
    if guess == winner:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You guessed correctly.")
        return True, 1
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You guessed wrong. Play again?")
        return False, 0


def game():
    game_playing = True
    score = 0
    while game_playing:
        person_A = random.choice(data)
        person_B = random.choice(data)
        while person_A == person_B:
            person_B = random.choice(data)
        print(logo)
        if score > 0:
            print(f"You're right! Current score: {score}")
        print(f"Compare A: {person_A['name']}, {person_A['description']}, {person_A['country']}. ")  
        print(vs)
        print(f"Compare B: {person_B['name']}, {person_B['description']}, {person_B['country']}. ")  
        
        winner = most_followers(person_A=person_A, person_B=person_B)
        guess = user_guess()
        game_playing, points = compare_guess(guess=guess, winner=winner)
        score += points

    play_again = input("Do you want to play again? Type 'Y' or 'N': ")
    if play_again == 'Y':
        game()

game()
    
