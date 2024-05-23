# You're a teacher inputting student grades into a system. In
# this practice, create a program that takes a student's
# grade as input and print feedback based on their performance:

# If the grade is 90 or more, display 'You’ve got an A!'
# If the grade is 80 or more, display '
# If the grade is 70 or more, display 'You’ve got a C!'
# If the grade is 60 or more, display 'You’ve got a D!'
# For anything less than 60, display 'You've got an F!'"

grade = int(input("Enter student's grade: "))
if grade>= 90:
    print("You’ve got an A!" )
elif grade>=80:
    print("You’ve got a B!")
elif grade>=70:
    print("display 'You’ve got a C!'")
elif grade >= 60:
    print("display 'You’ve got a d'")
else:
    print("display 'You've got an F!")