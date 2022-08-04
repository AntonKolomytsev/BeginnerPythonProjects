all_number = 0
for all_number in range(1,101):
    if all_number % 3 + all_number % 5 == 0:
        print("Fizz Buzz")
    elif all_number % 3 == 0:
        print("Fizz")
    elif all_number % 5 == 0:
        print("Buzz")
    else:
        print(all_number)

