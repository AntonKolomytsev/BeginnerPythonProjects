import random

coin_random = random.randint(0,1)
heads = "Heads".capitalize()
tails = "Tails".capitalize()
if coin_random == 0:
    print(f"{heads}")
else:
    print(f"{tails}")