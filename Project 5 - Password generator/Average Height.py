student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

a = 0
for count_item in student_heights:
  a += 1

total = 0
for x in student_heights:
  total += x


average_height = total / a
print(int(average_height))