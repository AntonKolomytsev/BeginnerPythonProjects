# print(len("56523"))
# Part 1
# Data Type
## Strings - "strings"
### "Moscow"[5]
### "12345" - strings too
# print("564" + "136")
# print("Hello" +" "+ "Rome")

## Integer - numbers
### 1234567890
# print(564+136)

## Float - value with point (Floating Point Number)
### 3.14159

## Boolean
### True or False

##TypeError - show errors into tje code, showes in console


## type defines type of variables
# num_char = len(input("What is your name?"))
# print(type(num_char))
# num_char = input("What is your name?")
# print(type(num_char))

### conversation from integer to string
# num_char = len(input("What is your name?"))
# new_num_char = str(num_char)
# print("Your name has" +" " + new_num_char + " " + "characters")

## integer + float

# a = float(123)
# print(type(a))
# print(200 + float(120.7))
# print(str(100) + str(300))

# #Part 2
# #Mathematical Operations
# a = float(150)
# print(type(a))
#
# print(str(100) + str(100))
# # Increase, decrease, multiply, devide(always we get float)
# # 5+6
# # 7-4
# # 3*2
# print(6/4)
# print(6/2)
# # ** Increase into exponent
# print(2**5)
# #PEMDAS
# #Parentheses - ()
# #Exponents - **
# #Multiplication - * Division - /
# #Addition - + Subtraction - -
# print(3*3+3/3-3)
# print(3*(3+3/3-3))
# ## Second desision
# print(3*(3+3)/3-3)

## PART 3
## Extra math's methods
print(8/3)
print(int(8/3))
# round returns whole number
print(round(8/3))
# , 2 points us numbers after dot
print(round(8/3, 2))
print(round(3.141565464, 3))
# Expression bellow defines type as integer
print(8 // 3)
#Expression bellow defines type as float
print(8 / 3)
# Expresions into variables /= , *=
result = 4 / 2
result /= 2
print(result)

#Expresions into variables += , -=
score = 0
score += 1
print(score)

# F-strings allows us mix strings among different date types
score = 0
height = 1.86
isWinning = True

# The way bellow between str
print("Your score is:" + str(score))

#f-string starts with f and variables stand into {}
print(f"Your score is: {score}, your height is {height}, you are winning is {isWinning}")
