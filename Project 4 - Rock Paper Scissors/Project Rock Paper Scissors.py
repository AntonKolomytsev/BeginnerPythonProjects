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

your_decide = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")

num_dec = int(your_decide)
if num_dec == 0:
    print(rock)
elif num_dec == 1:
    print(paper)
elif num_dec == 2:
    print(scissors)
else:
    print("You enter wrong number")

pc_game = random.randint(0, 2)
if pc_game == 2:
    print(scissors)
elif pc_game == 1:
    print(paper)
else:
    print(rock)



if num_dec >= 3 or num_dec < 0:
    print("You enter invalid number, you lose")
elif num_dec == 0 and pc_game == 0:
    print("You draw")
elif num_dec == 0 and pc_game == 1:
    print("You lost (")
elif num_dec == 0 and pc_game == 2:
    print("You win!")
elif num_dec == 1 and pc_game == 0:
    print("You win!")
elif num_dec == 1 and pc_game == 1:
    print("You draw")
elif num_dec == 1 and pc_game == 2:
    print("You lost (")
elif num_dec == 2 and pc_game == 0:
    print("You lost (")
elif num_dec == 2 and pc_game == 2:
    print("You draw")
elif num_dec == 2 and pc_game == 1:
    print("You win!")
else:
    print()

