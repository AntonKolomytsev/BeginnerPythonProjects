student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

best_score = 0
for a in student_scores:
    if a > best_score:
        best_score = a
print(f"The highest score in the class is: {best_score}")