print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name = name1 + name2
str.lower(name)
a = name.count('t')
b = name.count('r')
c = name.count('u')
d = name.count('e')
e = name.count('l')
f = name.count('o')
g = name.count('v')
h = name.count('e')

name_occurs_true = a + b + c + d
name_occurs_love = e + f + g + h
name_occurs_true = str(name_occurs_true)
name_occurs_love = str(name_occurs_love)

result = name_occurs_true + name_occurs_love
math_result = int(result)
print(math_result)
if math_result >= 40 and math_result <= 50:
    print(f"Your score is {math_result}, you are alright together.")
elif math_result <= 10 or math_result >=90:
    print(f"Your score is {math_result}, you go together like coke and mentos.")
else:
    print(f"Your score is {math_result}.")