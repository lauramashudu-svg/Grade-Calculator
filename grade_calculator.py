#grade calculator calculates the average and grade for a student

#get student name(user input)
student = input('Enter the your name: ')
marks = input('Enter your marks separated by spaces in between: ')

#convert the marks to a list of numbers
marks = [float(mark) for mark in marks.split()]

#calculate the average
average = sum(marks) / len(marks)

#determine grade
if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

#show results to 2 decimal places
print(f"\n{student}'s average: {average:.2f}")
print(f"{student}'s grade: {grade}")