names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
import random

who_will_pay = random.choices(names)
who_str = "".join(who_will_pay)

print(f"Guys be patient ))) Today will be pay {who_str}")

