print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

task1 = input("You are staying in the middle of trees. Where do you go? Please enter left or right\n").lower()

if task1 == "right":
    print("Go next")
    task2 = input("You see a river. Will you go along the river or swim across it? Please enter go or swim\n").lower()
    if task2 == "go":
        print("You are right again. Go along the river")
        task3 = input("You see four boxes. Red, Blue, Green and Orange. Enter first letter colors box that you choose.\n").lower()
        if task3 =="R":
            print("Congratulation. You find $10000  You win")
        elif task3 == "O":
            print("You find oranges. Bon appetite. You lose. But it isn't the worst option )")
        else:
            print("You were bitten a snake and you died. Game over")
    else:
        print("You were tried to swim across the river and you underwater. Game over ")
else:
    print("Game over")