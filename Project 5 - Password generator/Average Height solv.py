student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# Easy way
# total_height = sum(student_heights)
# count_students = len(student_heights)
# average_height = round(total_height / count_students)
# print(average_height)

total_height = 0
for height in student_heights:
  total_height += height

number_of_students = 0
for y in student_heights:
  number_of_students += 1

average_height = round(total_height/number_of_students)

print(average_height)

