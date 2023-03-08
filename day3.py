# Day 3, Rock, Paper, scissors

import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
db = [rock, paper, scissors]
user_input = int(input("Type 0 for rock, 1 for paper and 2 for scissors: "))
if user_input >= 3 or user_input < 0:
    print("Invalid Number, try again.")
hand1 = db[user_input]
print(f"Your hand:\n{hand1}")
computer_hand = random.randint(0,2)
hand2 = db[computer_hand]
print(f"Computer hand:\n{hand2}")
if computer_hand == 0 and user_input == 2: 
    print("You lost")
elif user_input == 0 and computer_hand == 2:
    print("You won")
elif computer_hand > user_input:
    print("You lost")
elif user_input > computer_hand:
    print("You won")
elif computer_hand == user_input:
    print("Draw")
