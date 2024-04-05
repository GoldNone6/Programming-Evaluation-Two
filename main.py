#inputting grades for each course and caulculating the average for user
course1 = float(input("Please enter the grade for course 1: "))
course2 = float(input("Please enter the grade for course 2: "))
course3 = float(input("Please enter the grade for course 3: "))
course4 = float(input("Please enter the grade for course 4: "))
average = round((course1+course2+course3+course4)/4, 2) 
grade = "error"

# loops to determine the level of the user
if average >= 95 and average <= 100:
 grade = "A+"

elif average >= 87 and average < 95:
 grade = "A"

elif average >= 80 and average < 87:
  grade = "A-"

elif average >= 77 and average < 80:
  grade = "B+"

elif average >= 72 and average < 77:
  grade = "B"

elif average >= 70 and average < 72:
  grade = "B-"

elif average >= 67 and average < 70:
  grade = "C+"

elif average >= 63 and average < 67:
  grade = "C"

elif average >= 60 and average < 63:
  grade = "C-"

elif average >= 57 and average < 60:
  grade = "D+"

elif average >= 54 and average < 57:
  grade = "D"

elif average >= 50 and average < 54:
  grade = "D-"

elif average >= 0 and average < 50:
  grade = "F"

else:
  print("error")

#outputting the average as a percentge and the level of the user
print("Your average for 4 courses is", average, "%" , "This is considered", grade,)
