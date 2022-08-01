print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

price_pizza = 0

if size == "S":
    price_pizza = 15
    if add_pepperoni == "Y":
        price_pizza += 5
        if extra_cheese == "Y":
            price_pizza += 1
            print(f"Your pizza will be cost ${price_pizza}")
if size == "M":
    price_pizza = 20
    if add_pepperoni == "Y":
        price_pizza += 3
        if extra_cheese == "Y":
            price_pizza += 1
            print(f"Your pizza will be cost ${price_pizza}")
if size == "L":
    price_pizza = 25
    if add_pepperoni == "Y":
     price_pizza += 3
    if extra_cheese == "Y":
        price_pizza += 1
    print(f"Your pizza will be cost ${price_pizza}")
print("We are sorry, come in next time")


