#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# Random select, then remove from the list.
password = []
rand_password = ""

# Select random numbers from range.

letter_pos = 0
sym_pos = 0
num_pos = 0 

# Generate Random Letters 
for x in range(1, (nr_letters +1)):
  letter_pos = random.randint(0, (len(letters)-1))
  password.append(letters[letter_pos])

# Generate random symbols
for x in range(1, (nr_symbols +1)):
  sym_pos = random.randint(0, (len(symbols)-1))
  password.append(symbols[sym_pos])

# Generate random numbers.
for x in range(1, (nr_numbers +1)):
  num_pos = random.randint(0, (len(numbers)-1))
  password.append(numbers[num_pos])

#Randomly mix password. 
random.shuffle(password)
for x in password:
  rand_password += x

print(f"Your password is: {rand_password}")


  



