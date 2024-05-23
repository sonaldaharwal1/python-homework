
# gpa = float(input("Enter your GPA: "))
#
# if gpa >= 3.5:
#     print("Congratulations, you're eligible for a scholarship!")
# elif gpa >= 3.0 and gpa <= 3.49:
#     print( "You're on the waiting list.")
# else:
#     print( "Keep up the good work.")



# age = int(input("Enter your age: "))
# child_ticket_price = 10
# adult_ticket_price = 20
# senior_ticket_price = 15
# free_admission_ticket_price= 0
#
# if age >=3 and age <=12:
#     print(f"Your ticket price is ${ child_ticket_price}")
# elif age>=13 and age <= 64:
#     print(f"Your ticket price is ${adult_ticket_price}")
# elif age >=65:
#      print(f"Your ticket price is ${senior_ticket_price}")
# else:
#     print("free admission")


# # Print ticket price
# annual_income = float(input("Enter your annual income: "))
# # Initialize variables for tax rates
# tax_rate_1 = 0.10  # 10%
# tax_rate_2 = 0.20  # 20
# tax_rate_3 = 0.30  # 30%
#
# if annual_income <= 40000:
#     print(f"Your tax amount is {tax_amount}"== annual_income * tax_rate_1)
# elif annual_income >= 40000 and annual_income<= 100000:
#     print((annual_income * tax_rate_2))
# elif annual_income >= 100000:
#     print( (annual_income * tax_rate_3))
#
# password = input("Enter your password: ")
#
# # Check password strength based on length
# if len(password) < 8:
#     print("Weak password.")
# elif len(password) >=8 and len(password) <= 12:
#     print("Moderate password.")

# course_code = input("Enter the course code: ")
#
# # Extract the last three characters of the course code
# course_ending = course_code[-3:].upper()
#
# # Take input for grade
# grade = input("Enter your grade for the course: ").upper()
#
# # Check eligibility based on course ending and grade
# if course_ending == "101" and grade in ["A", "B"]:
#     print("You are eligible to enroll in this course.")
# elif course_ending == "202" and grade in ["B", "C"]:
#     print("You are eligible to enroll in this course.")
# elif course_ending == "303" and grade in ["C", "D"]:
#     print("You are eligible to enroll in this course.")
# else:
#     print("You are not eligible to enroll in this course.")
# #     print("Strong password.")

# #
# frist_movie_rating = int(input("Enter the frist_movie_rating: "))
# second_movie_rating =int (input("Enter the second_movie_rating: "))
#
# if frist_movie_rating >= 7 and second_movie_rating >=7:
#     print("Let's watch both!")
# else:
#     print("Let's just pick one.")
#
# number = int(input("Enter the number: "))
# if number < 0:
#     print(number * -1)
# #
# #
# else:
#     print (number)
# number = int(input("Enter the number: "))
#
# if number % 3 == 0 and number % 7 == 0:
#     print('Bingo')
# elif number % 3 == 0:
#     print('Bin')
# elif number % 5 == 0:
#     print('Go')
# else:
#     print(number)
# x=1
# y =5
# z =3
# if x < y and x < z:
#     smallest = x
#     if y < z:
#         middle = y
#     else:
#         middle = z
# # Check if y is the smallest
# elif y < x and y < z:
#     smallest = y
#     if x < z:
#         middle = x
#     else:
#         middle = z
# # If neither x nor y is the smallest, z must be the smallest
# else:
#     smallest = z
#     if x < y:
#         middle = x
#     else:
#         middle = y
#
# print("The number that is neither the smallest nor the largest is:", middle)


# number = input("Enter a number: ")
#
# if number == number[::-1]:
#     print(True)
# else:
#     print(False)


# string = input("Enter a string: ")
# reversed_string = string[::-1]
# print(reversed_string)First_name = input('Enter your First_name: ')
# Last_name = input('Enter your Last_name: ')
# age = int(input('Enter your age: '))
# print("{First_name}{Last_name}".format(First_name =Last_name.title(), Last_name=Last_name.title() ,age=age))

# First_name = input('Enter your First_name: ')
# Last_name = input('Enter your Last_name: ')
# age = input('Enter your age: ')
# print("{First_name}{Last_name}".format(First_name =First_name.title(), Last_name=Last_name.title(),age=age))

my_list= ["ham", "bread", "cheese"]

# Write code that prints YES if the list contains "cheese".

if "cheess" in my_list:
    print("Yes")

