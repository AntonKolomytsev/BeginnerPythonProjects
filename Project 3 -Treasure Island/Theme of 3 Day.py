# Themes od Day 3
# Conditional Statements, Logical Operators, Code Blocks and Scope

## Theme 1 Controle Flow
### Пример с ванной и отдушкой. Пока НАБИРАЕТСЯ  вода ДО УРОВНЯ 80 сантиметров, мы продолжаем ее набирать,
### Если вода ДОСТИГЛА уровня 80 см мы имеем 2 варианта событий CЛИВАТЬ ее через отдушку или ОСТАНОВИТЬ ПОТОК.
### Conditional IF/ELSE
# !!!! if CONDITIONAL:
#        do this
#      else:
#        do this
water_level = 70
if water_level >80:
    print("Drain water")
else:
    print("Continue")

height = 130
if height >120:
    print("You can ride")
else:
    print("You can't ride")
## Theme 2 - Comparison Operators
### (x) > - greater than >= greater than or equal to
### (x)< - less than    <= - less than or equal to
### (x) ==  - equal to    != - not equal to

## Theme 3 - Nested if statements and elif statements (include into another condition)
###  For example : If you are less than 18 years old or equal, so price will be $7, if you are greater then 18 years old,
### so price will be $12
# if condition:
#     if another condition:
#         do this
#     else:
#         do this
# else:
#     do this

## Theme 4 - if/elif/else
# if condition1:
#     do A
# elif condition2:
#     do B
# else:
#     do this

## THEME 5 - Multiply if statements in Succesion

#  if/elif/else

# if condition1:
#     do A
# elif condition2:
#     do B
# else:
#     do C

# MULTIPLY CONDITIONS
# if condition1:
#     do A
# if condition2:
#     do B
# if condition3:
#     do C

## THEME 6 LOGICAL OPERATORS
# if condition1 & condition2 & condition3:
#    do this
# else:
#     do this
## and - if both conditions true we get true, if one of them false we get false
## or -  if one of them true we get true, we get false when both conditions are false
## not - making revers conditional
