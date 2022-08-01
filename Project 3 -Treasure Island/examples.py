print("Welcome to the our mountains bike school.")
height = int(input("What is your height in cm?:"))
bill = 0
if height > 120:
    print("Welcome to our school")
    age = int(input("How old are you?:"))
    if age <= 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    elif age <= 20:
        bill = 10
        print("Adult tickets are $10")
    elif age >= 60:
        bill = 0
        print("Retire tickets free")
    elif age >= 50 and age <= 53:
        bill = 1
        print("Special action. Ticket for you only $1")
    else:
        bill = 12
        print("Main tickets are $12")
    wants_extra_classes = input("Do you want an extra classes taken? Y or N.")
    if wants_extra_classes == "Y":
        # Add $5 to bill
        bill = bill + 5  # bill +=5

    print(f"Your total bill is ${bill}")


else:
    print("You can't learn in our school, come back throw 1 year")
